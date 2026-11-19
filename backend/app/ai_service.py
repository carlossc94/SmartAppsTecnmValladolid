import logging
import re
import httpx
from fastapi import HTTPException
from .config import ai_settings
from .providers.gemini import GeminiProvider
from .providers.deepseek import DeepSeekProvider
from .providers.groq import GroqProvider

logger = logging.getLogger('smartedu.ai')
PROVIDER_CLASSES = {'gemini': GeminiProvider, 'deepseek': DeepSeekProvider, 'groq': GroqProvider}

async def generate(prompt: str, max_tokens: int) -> str:
    settings = ai_settings()
    if settings.mode != 'real':
        raise HTTPException(503, detail='No hay un proveedor de IA activo; configura la API Key o utiliza modo demo')
    if not settings.model or not settings.base_url:
        raise HTTPException(500, detail=f'Configura {settings.provider.upper()}_MODEL y {settings.provider.upper()}_BASE_URL')
    if not re.fullmatch(r'[A-Za-z0-9_./:-]+', settings.model):
        raise HTTPException(400, detail='Nombre de modelo inválido')
    if not settings.base_url.startswith('https://'):
        raise HTTPException(500, detail='La URL del proveedor debe usar HTTPS')
    provider = PROVIDER_CLASSES[settings.provider](settings.key, settings.model, settings.base_url)
    try:
        async with httpx.AsyncClient(timeout=90) as client:
            result = await provider.generate(client, prompt, max_tokens)
        if not result:
            raise ValueError('Respuesta vacía')
        return result
    except httpx.HTTPStatusError as exc:
        status = exc.response.status_code
        # No registrar claves ni el cuerpo completo de una solicitud.
        logger.warning('%s HTTP %s: %s', settings.provider, status, exc.response.text[:600])
        message = {401: 'Clave de API inválida', 402: 'Saldo insuficiente',
                   429: 'Límite de solicitudes alcanzado', 503: 'Proveedor temporalmente no disponible'}.get(status, 'Error del proveedor')
        raise HTTPException(502, detail=f'{settings.provider.capitalize()} HTTP {status}: {message}') from None
    except httpx.HTTPError as exc:
        logger.warning('%s error de red: %s', settings.provider, type(exc).__name__)
        raise HTTPException(502, detail=f'No fue posible conectar con {settings.provider}') from None
    except (KeyError, IndexError, ValueError, TypeError, AttributeError):
        raise HTTPException(502, detail=f'{settings.provider.capitalize()} devolvió una respuesta inesperada') from None
