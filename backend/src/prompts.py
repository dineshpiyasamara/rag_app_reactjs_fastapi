qa_template = """You are an intelligent chatbot. Use the following pieces of information to answer the user's question.
If context and history not related to question, just say that you don't know, don't try to make up an answer.

Context: {context}
History: {history}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def generate_prompt(context, history, question):
    prompt = """You are an intelligent chatbot. Use the following pieces of information to answer the user's question.
    If context and history not related to question, just say that you don't know, don't try to make up an answer.

    Context: {}
    History: {}
    Question: {}

    Only return the helpful answer below and nothing else.
    Helpful answer:
    """.format(context, history, question)
    return prompt