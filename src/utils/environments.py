import os
from pathlib import Path
import sys
from typing import Dict, Union, Text
import openai
from dotenv import load_dotenv, find_dotenv
from constants import AZURE, NLTK_DATA, OPENAI_API_BASE, OPENAI_API_KEY, DEPLOYMENT_NAME,OPENAI_API_VERSION,GOOGLE_API_KEY
# from configs.config import WORKING_DIR, OPENAI_API_VERSION, VICUNA_API_KEY, VICUNA_API_BASE, NLTK_DATA_PATH, \
#     TIKTOKEN_CACHE_PATH
import logging
logger = logging.getLogger(__name__)



def set_working_dir(project_name:Union[Text, None] =None):
    if project_name:
        project_dir = Path.home().joinpath(project_name)
    else:
        script_path = os.path.abspath(__file__)
        project_dir = Path(script_path).parent.parent.absolute()
    os.chdir(project_dir)
    sys.path.extend([str(project_dir)])
    logger.info(f"working_dir={os.getcwd()}")
    # print(f"sys.path={sys.path}")
    return project_dir


def add_source_dir(source_dirname="src"):
    script_path = os.path.abspath(__file__)
    project_dir = Path(script_path).parent.parent.absolute()
    source_dir = str(project_dir / source_dirname)
    print(f"source_dir={source_dir}")
    sys.path.append(source_dir)


def load_env_variables_from_dotenv():
    _  = load_dotenv(find_dotenv(), override=True)
    #print(find_dotenv())
    env_variables = os.environ
    return env_variables


def set_gpt_env(use_openai=False,use_azure_openai=False, use_vicuna=False,
                use_gemini=True,
                set_proxy=True)-> Dict:
    if set_proxy:
        os.environ["http_proxy"] = "http://127.0.0.1:7890"
        os.environ["https_proxy"] = ""
        http_proxy = os.environ["http_proxy"]
        print(f"http_proxy={http_proxy}")

    env_variables = load_env_variables_from_dotenv()

    http_proxy = env_variables.get("http_proxy")
    https_proxy = env_variables.get("https_proxy")
    print(f"http_proxy={http_proxy}\nhttps_proxy={https_proxy}")
    # set working dir
    # os.chdir(WORKING_DIR)
    # logger.info(f"working_dir={WORKING_DIR}")

    # set nltk data path
    # os.environ[NLTK_DATA] = NLTK_DATA_PATH
    # os.environ[TIKTOKEN_CACHE_DIR] = TIKTOKEN_CACHE_PATH

    # add TESSERACT_PATH to env PATH
    # os.environ["PATH"] = os.environ["PATH"] +";" + os.environ["TESSERACT_PATH"]

    if use_openai:
        openai.api_key = os.getenv(OPENAI_API_KEY)

    elif use_azure_openai:
        openai.api_type = AZURE
        openai.api_version =os.getenv( OPENAI_API_VERSION)
        openai.api_key = os.getenv(OPENAI_API_KEY)
        openai.api_base= os.getenv(OPENAI_API_BASE)
        # if we use azure openai demplotment,we need to specific the deployment_name
        deployment_name =  os.getenv(DEPLOYMENT_NAME)
        logger.info(f"openai.api_type={openai.api_type}\nopenai.api_version={openai.api_version}")
    # elif use_vicuna:
    #     """
    #     https://huggingface.co/lmsys/vicuna-7b-v1.3
    #     """
    #     openai.api_key = VICUNA_API_KEY
    #     openai.api_base = VICUNA_API_BASE
    #     # explict set env for vicuna
    #     os.environ[OPENAI_API_KEY]  = VICUNA_API_KEY
    #     os.environ[OPENAI_API_BASE] =  VICUNA_API_BASE
    
    elif use_gemini:
        import google.generativeai as genai
        google_api_key =  os.getenv(GOOGLE_API_KEY)
        genai.configure(api_key=google_api_key)

    else:
        raise ValueError("not support gpt envriable")
        logger.info(f"openai.api_base={openai.api_base}")
    return env_variables