from sqlalchemy.orm import Session
from fastapi import  Depends,APIRouter
from datetime import datetime,date
from fastapi.responses import JSONResponse
from schemas.gpt_schemas import *
from config.gpt_config import chat_gpt
from config.prompt import recommendTarget_prompt, recommendTopic_prompt
import json

router = APIRouter()


@router.get('/test',tags=["gpt"],
    description="""
<h1>테스트 API</h1>

---
<h2>반환 값</h2>
- {'message' : 'connection complete !'}
             """ ,status_code=200)
def test_api():

    try:


        return JSONResponse({'message' : 'connection complete !'}, status_code = 200)
    
    except Exception as e:
        return JSONResponse({'error ' : e}, status_code = 400)


@router.post('/target',tags = ["gpt"],
             description = """
<h1>토론 대상 추천해주는 API</h1>
             """, status_code = 201)
def recommend_target(data : RecommendTarget):
    
    book_name = data.book_name
    
    #gpt에게 타겟 두명 물어보기.
    prompt = {"role" : "user", "content" : "소설 {}를 주제로 독서토론을 하고싶어.".format(book_name)}
    recommendTarget_prompt.append(prompt)
    data = chat_gpt(recommendTarget_prompt)

    return data

@router.post('/topic',tags = ["gpt"],
             description = """
<h1>토론 주제 추천해주는 API (2개 받아옴)</h1>
             """, status_code = 201)
def recommend_topic(data : RecommendTopic):
    
    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    
    prompt = {"role" : "user",
            "content" : "소설 {0}에서, {1}와 {2} 두 등장인물이 가상의 토론을 하려고해. 주제를 추천해줘.".format(book_name, sys_target, user_target)}
    recommendTopic_prompt.append(prompt)
    data = chat_gpt(recommendTopic_prompt)
    #gpt에게 질문해서 주제2개 받아오기.

    return JSONResponse({
        'topics' : data
    })

