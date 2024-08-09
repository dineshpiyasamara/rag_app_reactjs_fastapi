from pydantic import BaseModel
class ReqData(BaseModel):
    task_id: int = -1
    env: str = 'env'
    question_id: int = -1
    client_id: int = -1
    user_id: int = -1
    notification_id: int = -1
    chat_id: int = -1
    history_list: list = []
    question: str = ""
    file_url_list: list = []
    company_id: int = -1
    available_tokens: int = 0
    api_key: str = ''