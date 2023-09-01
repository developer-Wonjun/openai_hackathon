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


@router.post('/recommend/target',tags = ["gpt"],
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

@router.post('/recommend/topic',tags = ["gpt"],
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

#책
#토론 대상
#주제
@router.post('/recommend/question',tags = ["gpt"],
             description = """
<h1>n번 주제에 대한 질문 받아오는 API (3개 한번에 받아옴.) </h1>
             """, status_code = 201)
def recommend_question(data : RecommendQuestion):
    
    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    topic = data.topic
    
    #gpt한테, 질문 3개 불러오는 api
    
    questions = [
        '1번 질문입니다.',
        '2번 질문입니다.',
        '3번 질문입니다.'
    ]
    
    return JSONResponse({
        'questions' : questions
    })

#책
#토론 대상
#주제
#이번 회차의 질문
@router.post('/recommend/answer',tags = ["gpt"],
             description = """
<h1>n번 질문에 대한 답변 받아오는 API (2개 한번에 받아옴.) </h1>
             """, status_code = 201)
def recommend_answer(data : RecommendAnswer):
    
    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    topic = data.topic
    question = data.question
    
    #gpt한테 질문에 대한 답변 요구하기 (2개)
    # 받아오는 2개의 유형은 소통해서 정하기
    
    answers = [
        '1번 답변입니다.',
        '2번 답변입니다.'
    ]
    
    return JSONResponse({
        'answers' : answers
    })

#책
#토론 대상
#주제
#이번 회차의 질문
# 답변
@router.post('/recommend/feedback',tags = ["gpt"],
             description = """
<h1>답변에 대한 피드백 받아오는 API</h1>
             """, status_code = 201)
def recommend_answer(data : RecommendFeedback):
    
    book_name = data.book_name
    sys_target = data.sys
    user_target = data.user
    topic = data.topic
    question = data.question
    answer = data.answer
    self = data.self
    #gpt에게 해당 상황말하면서, 피드백 요구하기
    
    feedback = '제 생각은 ~~~~~~해서, ~~~~~~ 의견입니당!'
    
    sub_feedback = ''
    if self:
        # gpt한테, 본인이 직접 질문한 답변에 대해 의견 묻기
        sub_feedback = '@@라면 더 ~~스럽게 답변했을 거에요.'
    
    
    return JSONResponse({
        'feedback' : feedback,
        'sub_feedback' : sub_feedback
    })