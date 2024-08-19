from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from src.llms import openai_llm, azure_openai_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.entity import Query

app = FastAPI()

# declare origin/s
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/test")
async def test():
    return {"message": "Welcome to CodePRO LK!"}


@app.post("/api/ask_llm")
async def test_llm(request: Query):
    print("=================")
    print(request)
    query = request.question
    llm = azure_openai_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an helpful assistant. Please response to the queries"),
        ("user", "Question: {question}")
    ])

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    response = chain.invoke({'question': query})
    print(response)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
