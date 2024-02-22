import os
import pathlib
import textwrap
from typing import Text,List


import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.ai.generativelanguage as glm


import langchain
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langchain.prompts import PromptTemplate
# from langchain.document_loaders import WebBaseLoader
from langchain.schema import StrOutputParser,HumanMessage,AIMessage,SystemMessage,ChatMessage,BaseMessage
from langchain.schema.prompt_template import format_document
from langchain.chains import LLMChain




def chat_with_google_genai():
  """
  roles: user + model
  https://ai.google.dev/tutorials/python_quickstart#chat_conversations
  
  """
  # Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
  # GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')

  for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
      print(m.name)


  # The ChatSession class simplifies the process by managing the state of the conversation, so unlike with generate_content, you do not have to store the conversation history as a list.
  model = genai.GenerativeModel('gemini-pro')
  chat = model.start_chat(history=[])

  # response = chat.send_message("In one sentence, explain how a computer works to a young child.")

  generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=['x'],
        max_output_tokens=20,
        temperature=1.0)
  
  safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }


  response = chat.send_message("In one sentence, explain how a computer works to a young child.",
                               generation_config=generation_config,
                              stream=True,
                              safety_settings=safety_settings)

  for chunk in response:
    print(chunk.text)
    print("_"*80)


  # for message in chat.history:
  #   display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))

def chat_gemini_with_llm(text="你能做什么",model="gemini-pro", temperature=0.7, top_p=0.85 )->Text:
  """
  we need to make prompt engineering:
  1. short the answer to match the hunman (gemini's answer is too long sometimes)
  2. postprogresss: remove the '*' char

  https://python.langchain.com/docs/integrations/chat/google_generative_ai
  """
  llm = ChatGoogleGenerativeAI(model=model,temperature=temperature, top_p= top_p )

  result = llm.invoke(text)
  result_content = result.content
  print(f"model={model}\ninput: text,\noutput: {result_content}\n{'*'*100}")
  return result_content



def tranlate_gemini_with_chain():
  """
  https://github.com/google/generative-ai-docs/blob/main/examples/gemini/python/langchain/Gemini_LangChain_QA_Chroma_WebLoad.ipynb
  """

  llm = ChatGoogleGenerativeAI(model="gemini-pro",
                 temperature=0.7, top_p=0.85)

  # To query Gemini
  llm_prompt_template = """translate the flowing text to {language}:
  "{input_text}"
  TRANSLATION:"""
  llm_prompt = PromptTemplate.from_template(llm_prompt_template)
  print(llm_prompt)

  chain = LLMChain(llm=llm, prompt=llm_prompt)
  output = chain.invoke(input={"input_text": "I love learning deep learning","language":"chinese"})
  output_text = output["text"]
  print(f"output_text={output_text}")
  return output



class ChatGemini():
  """
  roles=("user", "model")
  """
  def __init__(self, model="gemini-pro", temperature=0.7, top_p=0.85 ):
    self.model = model
    self.temperature = temperature
    self.top_p =top_p
    self.llm =  ChatGoogleGenerativeAI(model=model,temperature=temperature, top_p= top_p)

    self.max_words=30
    self.start_message = self._build_start_message()


  
  def _build_start_message(self)-> HumanMessage:
      ai_message_template = f"你的名字叫 芬奇，你是一个有用，友好，幽默的助手，乐于帮助人们回答各种问题，你的回答不应该超过{self.max_words}词语"
      message = HumanMessage(content=ai_message_template)
      return message
      

  def _build_messages(self,text:Text)->List[BaseMessage]:
      # template = """You a helpfule assitant to answer the question from human, your answer should not be less than {length} words,
      # the input text is {text}"""
      # prompt_template = PromptTemplate.from_template(template)
      # prompt_template =  PromptTemplate(input_variables=["length","text"],template=template)
      # prompt = prompt_template.format(text = text,length = self.length)
      # prompt = prompt_template.format_prompt(text = text,length = self.length)
      # prompt_str =prompt.to_string()
      # messages = prompt.to_messages()
      ai_message = AIMessage(content="OK")
      human_message = HumanMessage(content=text)
      messages = [self.start_message,ai_message, human_message]
      return messages


  def chat(self, text:Text="你能做什么啊")-> Text:
      messages = self._build_messages(text=text)
      ai_message = self.llm.invoke(messages)
      result_content = ai_message.content
      print(f"model={self.model}\ninput: text,\noutput: {result_content}\n{'*'*100}\nYou can start a new turn chat now")
      return result_content
  




if  __name__ =="__main__":
  from utils.environments import set_gpt_env
  set_gpt_env()
  # chat_with_google_genai()
  # output = chat_gemini_with_llm()

  chat_gemini = ChatGemini()
  output =  chat_gemini.chat()
  print(f"output={output}")
  