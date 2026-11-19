from abc import ABC, abstractmethod
import httpx

class AIProvider(ABC):
    @abstractmethod
    async def generate(self, client: httpx.AsyncClient, prompt: str, max_tokens: int) -> str:
        ...
