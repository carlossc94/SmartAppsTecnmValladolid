import httpx
from .base import AIProvider

class GeminiProvider(AIProvider):
    def __init__(self, key: str, model: str, base_url: str):
        self.key, self.model, self.base_url = key, model.removeprefix('models/'), base_url

    async def generate(self, client: httpx.AsyncClient, prompt: str, max_tokens: int) -> str:
        response = await client.post(
            f'{self.base_url}/models/{self.model}:generateContent',
            headers={'x-goog-api-key': self.key},
            json={'contents': [{'parts': [{'text': prompt}]}],
                  'generationConfig': {'temperature': 0.2, 'maxOutputTokens': max_tokens}},
        )
        response.raise_for_status()
        parts = response.json()['candidates'][0]['content']['parts']
        return '\n'.join(part['text'] for part in parts if 'text' in part).strip()
