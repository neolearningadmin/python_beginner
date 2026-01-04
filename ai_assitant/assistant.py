import os
from openai import OpenAI

class OpenAIAssistant:
    def __init__(self, model="gpt-3.5-turbo", api_key=None):
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else OpenAI()
        self.model = model

    def ask(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
        )
        return resp.choices[0].message.content.strip()