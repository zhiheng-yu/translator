import os
from agno.agent import Agent
from agno.models.openai import OpenAILike


local_dir = os.path.dirname(__file__)
system_prompt_path = os.path.join(local_dir, "config", "translate_prompt.md")
with open(system_prompt_path, "r", encoding='utf-8') as f:
    system_prompt = f.read()

llm_model = OpenAILike(
    id=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
)

translate_agent = Agent(
    model=llm_model,
    name="translate_agent",
    description="A translate agent that translates the text",
    instructions=[system_prompt]
)

def translate(text, dst_lang):
    request = text + " -> dst_lang: " + dst_lang
    run_output = translate_agent.run(request, stream=False)
    return run_output.content

if __name__ == '__main__':
    dst_lang = input("目标语言: ")
    text = input("需要翻译的文本: ")
    result = translate(text, dst_lang)
    print(result)
