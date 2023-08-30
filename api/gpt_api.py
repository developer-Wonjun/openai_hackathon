from sqlalchemy.orm import Session
from fastapi import  Depends,APIRouter
from datetime import datetime,date
from fastapi.responses import JSONResponse
router = APIRouter()


@router.get('/test',tags=["user"],
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
