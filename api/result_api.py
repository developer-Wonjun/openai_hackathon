from sqlalchemy.orm import Session
from fastapi import  Depends,APIRouter
from datetime import datetime,date
from fastapi.responses import JSONResponse
from schemas.gpt_schemas import *
from config.gpt_config import chat_gpt
from config.prompt import getScore_prompt, getSummary_prompt

router = APIRouter()


@router.post('',tags = ["result"],
             description = """
<h1>토론 요약 서평 받아오는 API</h1>
             """, status_code = 201)
def get_result(data : RecommendResult):

    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    topic = data.topic
    answers = data.answers
    feedbacks = data.feedbacks

    score_prompt = {"role" : "user",
        "content" : f"{book_name}라는 소설을 주제로 '{user_target}'과 '{sys_target}' 두 인물이 {topic}'의 주제로 가상토론을 하고있어.\
            이때, '{user_target}'가\
                1. {answers[0]}\
                2. {answers[1]}\
                3. {answers[2]} 라는 주장을 내세웠을때, \
            이 3가지 주장이 소설속 '{user_target}'의 사고 얼마나 유사할까?\
        "}
    getScore_prompt.append(score_prompt)
    score = chat_gpt(getScore_prompt)
    
    result_prompt = {"role" : "user",
        "content" : f"{book_name}라는 소설을 주제로 '{user_target}'과 '{sys_target}' 두 인물이 {topic}'의 주제로 가상토론을 하고있어.\
            이때, '{sys_target}'가\
                1. {feedbacks[0]}\
                2. {feedbacks[1]}\
                3. {feedbacks[2]} 라는 피드백을 내세웠을 때, \
            이 3가지 피드백을 한문장으로 요약해줘\
        "}
    getSummary_prompt.append(result_prompt)
    result = chat_gpt(getSummary_prompt)

    
    
    return JSONResponse({
        'score' : score['score'],
        'user_summary' : score['result'],
        'sys_summary' : result['result']
    })