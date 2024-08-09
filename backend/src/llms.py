from langchain_openai import AzureChatOpenAI
from langchain_openai import ChatOpenAI
from params import *
from dotenv import load_dotenv
import os

load_dotenv()


def openai_llm():
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model=llm_model_name,
        temperature=0
    )
    return llm


def azure_openai_llm():
    llm = AzureChatOpenAI(
        model=llm_model_name,
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT")

    )
    return llm
