from sqlalchemy.orm import Session
from fastapi import  Depends,APIRouter
from datetime import datetime,date
from fastapi.responses import JSONResponse
from schemas.gpt_schemas import *

router = APIRouter()


@router.post('',tags = ["result"],
             description = """
<h1>토론 요약 서평 받아오는 API</h1>
             """, status_code = 201)
def get_result(data : RecommendResult):
    
    
    return JSONResponse({
        'score' : 88,
        'summary' : '한줄 요약',
        'perspective' : {
            'user' : '참여자 관점',
            'sys' : '시스템 관점'
        },
        'moral' : '교훈'
    })