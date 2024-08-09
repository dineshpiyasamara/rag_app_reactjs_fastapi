from langchain_openai import AzureChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from params import *
from dotenv import load_dotenv
import os

load_dotenv()


def openai_llm():
    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model=LLM_MODEL_NAME,
        temperature=0
    )
    return llm


def azure_openai_llm():
    llm = AzureChatOpenAI(
        model=LLM_MODEL_NAME,
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT")
    )
    return llm


def embedding_model():
    embedding_model = OpenAIEmbeddings(model=EMBEDDING_MODEL_NAME)
    return embedding_model
