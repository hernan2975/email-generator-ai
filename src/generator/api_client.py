
import openai
from .exceptions import APIError
from loguru import logger

class OpenAIClient:
    def __init__(self, api_key: str):
        self.client = openai.Client(api_key=api_key)
    
    def send_prompt(self, prompt: str, model: str = "gpt-4") -> str:
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"API Error: {e}")
            raise APIError("Failed to connect to OpenAI API")
