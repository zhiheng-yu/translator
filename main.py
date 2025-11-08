from translate_agent import OpenAIAgent

if __name__ == '__main__':
    dst_lang = input("选择翻译的目标语言: ")
    agent = OpenAIAgent(dst_lang=dst_lang)

    while True:
        src_text = input("输入需要翻译的文本: ")

        if src_text == "/q":
            break

        response = agent.translate(src_text)
        print(response)
