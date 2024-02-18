import os
import pathlib
import textwrap

from utils.environments import set_gpt_env
set_gpt_env()

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.ai.generativelanguage as glm


import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
# from langchain.document_loaders import WebBaseLoader
from langchain.schema import StrOutputParser
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
    

def chat_gemini_with_langchain():
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





if  __name__ =="__main__":
  # chat_with_google_genai()
  chat_gemini_with_langchain()