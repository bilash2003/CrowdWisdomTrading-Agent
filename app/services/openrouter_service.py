import os
from openai import OpenAI
from app.utils.config import OPENROUTER_API_KEY, OPENROUTER_MODEL


class OpenRouterService:

    def __init__(self):
        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

    def ask(self, prompt: str):

        response = self.client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content