#-*- coding:utf-8 -*-

recommendTarget_prompt =[
    {"role" : "system",
     "content" : "토론 대상을 추천해줄때에는, 책의 저자 혹은 책에서 중요한 역할로 하는 인물 중 가치관이 대립하는 인물 2명 추천해줘.\
        또 다른 부연 설명 없이, {'target1':{'name': '', 'role': '',},'target2':{'name': '','role': ''},'reason':'' }의 형식으로만 대답해줘야해.\
        name은 추천해주는 인물의 이름, role은 그 인물의 짧막한 설명이야. reason은 두 인물의 가치관이 대립하는 이유야."},

    {"role" : "user",
     "content" : "책 '일리아드'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'아킬레우스', 'role':'자신의 명예를 중요시한다.'}, 'target2':{'name':'헥토르', 'role' : '나라와 가족을 지키기 위해 싸우는 책임감 있는 인물'}, 'reason':'이 둘은 명예와 책임, 개인과 공동체 등에서 대립하는 가치관을 보입니다.'}"},
    {"role" : "user",
     "content" : "책 '신곡'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'덴테', 'role':'자신을 구원하려는 목적을 가지고 있다.'}, 'target2':{'name':'루시페르', 'role' : '지옥의 군주'}, 'reason':'구원과 타락이라는 대립되는 가치관을 가진 이 두 인물은 작품에서 중요한 역할을 합니다.'}"},

    {"role" : "user",
     "content" : "책 '돈키호테'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'돈키호테', 'role':'이상주의와 로맨스를 추구'}, 'target2':{'name':'산초 판자', 'role' : '현실주의와 실용성을 중시'}, 'reason':'이상과 현실, 로맨스와 실용성에서 대립하는 가치관을 가집니다.'}"},

    {"role" : "user",
     "content" : "책 '햄릿'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'햄릿', 'role':'진실을 추구하고 복수를 원함.'}, 'target2':{'name':'클라우디우스', 'role' : '권력을 장악하기위해 거짓과 배신을 사용.'}, 'reason':'복수와 용서, 진실과 거짓이 대립하는 가치관을 가지고 있습니다.'}"},

    {"role" : "user",
     "content" : "책 '안나 카레니나'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'안나 카레니나', 'role':'개인적인 행복과 자유를 추구'}, 'target2':{'name':'알렉세이 카레닌', 'role' : '사회적인 도덕과 규범을 중시'}, 'reason':'이 둘은 개인의 자유와 사회적 도덕이라는 대립되는 가치관을 가지고 있습니다.'}"},

    ]