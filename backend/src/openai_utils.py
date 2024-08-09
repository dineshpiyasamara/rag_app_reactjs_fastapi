import openai
import os
import tiktoken


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def check_openai_api_key(api_key):
    client = openai.OpenAI(api_key=api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True


def check_openai_api_key_expirity(api_key):
    print(api_key)
    try:
        os.environ["OPENAI_API_KEY"] = api_key
        client = openai.OpenAI(
            api_key=api_key,
        )
        chat_completion = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {'role': 'user', 'content': 'This is test'}
            ],
            max_tokens=5
        )
    except Exception as e:
        print(e)
        return False
    else:
        return True
