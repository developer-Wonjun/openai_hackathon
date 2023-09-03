from sqlalchemy.orm import Session
from fastapi import  Depends,APIRouter
from datetime import datetime,date
from fastapi.responses import JSONResponse
from schemas.gpt_schemas import *
from config.gpt_config import chat_gpt
from config.prompt import getQuestion_prompt, getAnswer_prompt, getFeedback_prompt
from datetime import datetime

router = APIRouter()

#책
#토론 대상
#주제
@router.post('/question',tags = ["chat"],
             description = """
<h1>n번 주제에 대한 질문 받아오는 API (3개 한번에 받아옴.) </h1>
             """, status_code = 201)
def get_question(data : RecommendQuestion):
    
    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    topic = data.topic
    
    #gpt한테, 질문 3개 불러오는 api
    
    prompt = {
        "role" : "user",
        "content" : f"소설 '{book_name}'에서 대립하는 '{sys_target}'와 '{user_target}' 두 인물이 '{topic}'의 주제를 토대로 가상 토론을 하려해. 토론을 나눌만한 3가지 질문을 추천해줘."
    }
    getQuestion_prompt.append(prompt)
    data = chat_gpt(getQuestion_prompt)
    return data

#책
#토론 대상
#주제
#이번 회차의 질문
@router.post('/answer',tags = ["chat"],
             description = """
<h1>n번 질문에 대한 답변 받아오는 API (2개 한번에 받아옴.) </h1>
             """, status_code = 201)
def get_answer(data : RecommendAnswer):
    start = datetime.now()
    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    topic = data.topic
    question = data.question
    
    #gpt한테 질문에 대한 답변 요구하기 (2개)
    # 받아오는 2개의 유형은 소통해서 정하기
    prompt = {
        "role" : "user",
        "content" : f"소설 '{book_name}'에서 대립하는 '{sys_target}'와 '{user_target}' 두 인물이 토론을 하고있어. '{question}'라는 {sys_target}의 질문에 {user_target} 입장에서 대답할 수 있는 답변1개, {sys_target} 입장에서 대답할 수 있는 답변 1개를 각각 알려줘."
        # 'content' : f"In the novel '{book_name}' provide one answer each from the perspectives of '{sys_target}' and '{user_target}' to {sys_target}'s question, '{question}'"
    }
    getAnswer_prompt.append(prompt)
    data = chat_gpt(getAnswer_prompt)

    print(datetime.now() - start)
    return data

# body 한글
# 한글 -> 영어 (3.5)
# 영어로 gpt4를 타고
# 영어 -> 한글

#책
#토론 대상
#주제
#이번 회차의 질문
# 답변
@router.post('/feedback',tags = ["chat"],
             description = """
<h1>답변에 대한 피드백 받아오는 API</h1>
             """, status_code = 201)
def get_feedback(data : RecommendFeedback):
    
    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    topic = data.topic
    question = data.question
    answer = data.answer
    self = data.self
    #gpt에게 해당 상황말하면서, 피드백 요구하기
    
    prompt = {
        "role" : "user",
        "content" : f"소설 '{book_name}'를 주제로 '{sys_target}'와 '{user_target}'  가상의 독서토론을 나누고 있어. '{question}'라는 {sys_target}의 질문에 '{answer}'라고 {user_target}가 답변을 했어. {user_target}의 답변에대한 {sys_target}의 피드백을 부탁해"
        }
    
    getFeedback_prompt.append(prompt)
    data = chat_gpt(getFeedback_prompt)

    
    feedback = '제 생각은 ~~~~~~해서, ~~~~~~ 의견입니당!'
    
    sub_feedback = ''
    if self:
        # gpt한테, 본인이 직접 질문한 답변에 대해 의견 묻기
        sub_feedback = '@@라면 더 ~~스럽게 답변했을 거에요.'
    
    
    return JSONResponse({
        'feedback' : data,
        'sub_feedback' : sub_feedback
    })