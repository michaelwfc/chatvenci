# pip install openai
import openai


class OpenaiChatBot:
    def __init__(self):
        self.conversations = [
                                {"role": "system", "content": "你是用户user的好朋友，能够和user进行愉快的交谈，你的名字叫Murphy."}
                            ]

    def chat(self, text):
        text = text.replace('\n', ' ').replace('\r', '').strip()
        if len(text) == 0:
            return
        print(f'chatGPT Q:{text}')
        self.conversations.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # model="gpt-4",
            messages=self.conversations,
            max_tokens=2048,
            temperature=0.3,
        )
        reply = response.choices[0].message.content
        self.conversations.append({"role": "assistant", "content": reply})
        return reply



if __name__ == '__main__':
    from utils.environments import set_gpt_env
    set_gpt_env()
    openai_chatbot = OpenaiChatBot()
    print(openai_chatbot.chat('你好，你叫什么?'))
    # print(openai_chatbot.chat('天空为什么是蓝色的?'))
