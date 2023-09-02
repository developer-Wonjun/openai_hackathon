from sqlalchemy.orm import Session
from fastapi import  Depends,APIRouter
from datetime import datetime,date
from fastapi.responses import JSONResponse
from schemas.gpt_schemas import *

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
    
    target1 = "헤르만 헤세"
    target2 = "프리드리히 니체"
    
    return JSONResponse({
        'target1' : target1,
        'target2' : target2
    })

@router.post('/topic',tags = ["gpt"],
             description = """
<h1>토론 주제 추천해주는 API (2개 받아옴)</h1>
             """, status_code = 201)
def recommend_topic(data : RecommendTopic):
    
    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    
    #gpt에게 질문해서 주제2개 받아오기.
    topics = [
        '1번 주제입니다.',
        '2번 주제입니다.'
    ]
    
    return JSONResponse({
        'topics' : topics
    })

