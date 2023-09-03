from typing import List, Union,Optional
from fastapi import UploadFile,Form
from pydantic import BaseModel
from datetime import datetime

class InsertBookname(BaseModel):
    book_name:str

class RecommendTarget(InsertBookname):
    pass

class RecommendTopic(InsertBookname):
    sys:str
    user:str
    
class RecommendQuestion(RecommendTopic):
    topic:str

class RecommendAnswer(RecommendQuestion):
    question : str
    
class RecommendFeedback(RecommendAnswer):
    answer : str
    self : bool
    
class RecommendResult(RecommendQuestion):
    answers : list
    feedbacks : list

# 1. <h1>n번 주제에 대한 질문 받아오는 API </h1>
# 2. <h1>n번 주제에 대한 답변2개를 받아오는 API </h1>
# 3. <h1>n번 주제에 답변에 대한 피드백 받아오는 API </h1>