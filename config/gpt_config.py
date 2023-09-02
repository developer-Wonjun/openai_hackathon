#-*- coding:utf-8 -*-
import os
import openai
import json

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
    replace_content = content.replace("'","\"")
    json_content = json.loads(replace_content)

    return json_content



