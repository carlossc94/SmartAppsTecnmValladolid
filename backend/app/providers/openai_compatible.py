import httpx
from .base import AIProvider

class OpenAICompatibleProvider(AIProvider):
    """Contrato chat/completions compartido por DeepSeek y Groq."""
    def __init__(self, key: str, model: str, base_url: str):
        self.key, self.model, self.base_url = key, model, base_url

    async def generate(self, client: httpx.AsyncClient, prompt: str, max_tokens: int) -> str:
        response = await client.post(
            f'{self.base_url}/chat/completions',
            headers={'Authorization': f'Bearer {self.key}'},
            json={'model': self.model, 'messages': [{'role': 'user', 'content': prompt}],
                  'temperature': 0.2, 'max_tokens': max_tokens, 'stream': False},
        )
        response.raise_for_status()
        return (response.json()['choices'][0]['message']['content'] or '').strip()
