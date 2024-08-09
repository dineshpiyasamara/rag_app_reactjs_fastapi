from fastapi import FastAPI
from src.llms import openai_llm, azure_openai_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()


@app.get("/api/test")
async def test():
    return {"message": "Welcome to CodePRO LK!"}


@app.get("/api/test_llm")
async def test_llm():
    query = "hello. how are you"
    llm = azure_openai_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an helpful assistant. Please response to the queries"),
        ("user", "Question: {question}")
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    response = chain.invoke({'question': query})
    print(response)
    return {"message": response}
