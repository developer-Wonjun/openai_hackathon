#-*- coding:utf-8 -*-
import os
import openai
import json
from datetime import datetime

openai.organization = "org-pNPql1ZvbYcYpx3hQewDKmii"
# try:
openai.api_key = os.getenv("OPENAI_API_KEY")
# except:
openai.Model.list()



def chat_gpt(message):
    gpt = openai.ChatCompletion.create(
    # 사용 모델
    model="gpt-4",
    # 전달 메세지
    messages=message,
    temperature = 0.7,
    )
    content = gpt['choices'][0]['message']['content']
    start = datetime.now()
    
    try:
        replace_content = content.replace("'","\"")
        json_content = json.loads(replace_content)
    except:
        json_content = content
    print('변환 시간 : ', datetime.now() - start)
    return json_content



