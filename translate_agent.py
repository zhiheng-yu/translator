import os
from openai import OpenAI


class TranslateAgent:
    def __init__(self, dst_lang="English"):
        local_dir = os.path.dirname(__file__)

        system_prompt_path = os.path.join(local_dir, "config", "translate_prompt.md")
        with open(system_prompt_path, "r", encoding='utf-8') as f:
            self.system_prompt = f.read()

        self.dst_lang = dst_lang
        self.system_prompt = self.system_prompt.replace("{{dst_lang}}", self.dst_lang)

    def generate(self, messages):
        raise NotImplementedError

    def translate(self, text):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text},
        ]

        return self.generate(messages)


class OpenAIAgent(TranslateAgent):
    def __init__(self, dst_lang="English"):
        super().__init__(dst_lang)
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        )

    def generate(self, messages):
        response = self.client.chat.completions.create(
            model="qwen3-30b-a3b-instruct-2507",
            messages=messages,
            stream=False
        )

        if response.choices and len(response.choices) > 0:
            return response.choices[0].message.content
        else:
            return ""
