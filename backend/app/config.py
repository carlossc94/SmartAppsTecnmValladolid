import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
from fastapi import HTTPException

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env', override=True)
PROMPTS = BASE_DIR / 'prompts'
CONTEXTS = BASE_DIR / 'contexts'
PROVIDERS = {'gemini', 'deepseek', 'groq'}

@dataclass(frozen=True)
class AISettings:
    provider: str
    key: str
    model: str
    base_url: str
    mode: str


def ai_settings() -> AISettings:
    provider = os.getenv('AI_PROVIDER', 'demo').strip().lower()
    if provider not in PROVIDERS | {'demo'}:
        raise HTTPException(500, detail='AI_PROVIDER debe ser demo, gemini, deepseek o groq')
    if provider == 'demo':
        return AISettings('demo', '', '', '', 'demo')
    prefix = provider.upper()
    key = os.getenv(f'{prefix}_API_KEY', '').strip()
    model = os.getenv(f'{prefix}_MODEL', '').strip()
    base_url = os.getenv(f'{prefix}_BASE_URL', '').strip().rstrip('/')
    # Sin clave se usa modo demostración, como en el proyecto original.
    return AISettings(provider, key, model, base_url, 'real' if key else 'demo')
