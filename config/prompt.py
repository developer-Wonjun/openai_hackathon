#-*- coding:utf-8 -*-

recommendTarget_prompt =[
    {"role" : "system",
     "content" : "토론 대상을 추천해줄때에는, 책의 저자 혹은 책에서 중요한 역할로 하는 인물 중 가치관이 대립하는 인물 2명 추천해줘.\
        또 다른 부연 설명 없이, {'target1':{'name': '', 'role': '',},'target2':{'name': '','role': ''},'reason':'' }의 형식으로만 대답해줘야해.\
        name은 추천해주는 인물의 이름, role은 그 인물의 짧막한 설명이야. reason은 두 인물의 가치관이 대립하는 이유야."},

    {"role" : "user",
     "content" : "책 '일리아드'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'아킬레우스', 'role':'자신의 명예를 중요시하는,'}, 'target2':{'name':'헥토르', 'role' : '책임감 있는 인물인,'}, 'reason':'이 둘은 명예와 책임, 개인과 공동체 등에서 대립하는 가치관을 보입니다.'}"},
    {"role" : "user",
     "content" : "책 '신곡'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'덴테', 'role':'자신을 구원하려는 목적을 가진,'}, 'target2':{'name':'루시페르', 'role' : '지옥의 군주,'}, 'reason':'구원과 타락이라는 대립되는 가치관을 가진 이 두 인물은 작품에서 중요한 역할을 합니다.'}"},

    {"role" : "user",
     "content" : "책 '돈키호테'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'돈키호테', 'role':'이상주의와 로맨스를 추구하는,'}, 'target2':{'name':'산초 판자', 'role' : '현실주의와 실용성을 중시하는,'}, 'reason':'이상과 현실, 로맨스와 실용성에서 대립하는 가치관을 가집니다.'}"},

    {"role" : "user",
     "content" : "책 '햄릿'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'햄릿', 'role':'진실을 추구하고 복수를 원하는,'}, 'target2':{'name':'클라우디우스', 'role' : '권력을 장악하기위해 거짓과 배신을 사용하는,'}, 'reason':'복수와 용서, 진실과 거짓이 대립하는 가치관을 가지고 있습니다.'}"},

    {"role" : "user",
     "content" : "책 '안나 카레니나'를 주제로 독서토론을 하고싶어." },
    {"role" : "assistant",
     "content" : "{'target1' : {'name':'안나 카레니나', 'role':'개인적인 행복과 자유를 추구하는,'}, 'target2':{'name':'알렉세이 카레닌', 'role' : '사회적인 도덕과 규범을 중시하는,'}, 'reason':'이 둘은 개인의 자유와 사회적 도덕이라는 대립되는 가치관을 가지고 있습니다.'}"},

    ]


recommendTopic_prompt = [
    {"role" : "system",
     "content" : "토론의 주제를 추천해줄 때에는, 교육적으로 의미 있는 것 2가지를 문장 형태로 추천해 주고,각자 어떤 입장인지 각각 주제에 대해서 설명해 줘.\
         그리고 답변은 ['', '']의 형식으로 부탁해.\
        ['', ''] 외에 그 어떤 부연설명도 하지 말아줘."},
    
    {"role" : "user",
     "content" : "소설 '파우스트'에서 '파우스트'와 '메피스토펠레스' 두 등장인물이 가상의 토론을 하려고해 주제를 추천해줘. " },
    {"role" : "assistant",
     "content" : "['지식은 인간을 자유롭게 만드는가, 아니면 더 큰 노예로 만드는가?', '도덕성이 상대적인가, 절대적인가?']"},
  
    {"role" : "user",
     "content" : "소설 '죄와벌'에서 '라스콜니코프'와 '소니아' 두 등장인물이 가상의 토론을 하려고해 주제를 추천해줘. " },
    {"role" : "assistant",
     "content" : "['구원은 자기 스스로 할 수 있는가, 아니면 외부의 도움이 필요한가?', '도덕적으로 허용된 살인은 존재하는가?']"}
]

getQuestion_prompt = [
    {"role" : "system",
     "content" : "토론의 질문을 추천해줄 때에는, 주제를 바탕으로 3개자 추천해줘. 또 토론 대상 두명이 소설 속에서 대립하는 인물이므로, 이러한 대립이 잘 나타났으면해.\
         그리고 답변은 ['', '', '']의 형식으로 부탁해."},
    
    {"role" : "user",
    "content" : "소설 '파우스트'에서 대립하는 '메피스토펠레스'와 '파우스트' 두 인물이 '도덕성이 상대적인가, 절대적인가?'의 주제를 토대로 가상 토론을 하려해. 토론을 나눌만한 3가지 질문을 추천해줘."},
    {"role" : "assistant",
     "content" : "['윤리적 기준은 자연법에 의해 결정되는가, 아니면 사회와 문화에 의해 형성되는가?', '인간은 자신의 욕망을 충족시키기 위해 어디까지 갈 수 있는가? 이에는 도덕적한 한계가 있는가?', '개인의 행복과 사회의 복지 중 어느 것이 더 중요한가? 이 둘 사이에는 절대적인 가치 판단이 가능한가?']"},
    
    {"role" : "user",
    "content" : "소설 '죄와벌'에서 대립하는 '라스콜니코프'와 '소니아' 두 인물이 '구원은 자기 스스로 할 수 있는가, 아니면 외부의 도움이 필요한가?'의 주제를 토대로 가상 토론을 하려해. 토론을 나눌만한 3가지 질문을 추천해줘."},
    {"role" : "assistant",
     "content" : "['구원은 개인의 내면적인 변화로만 이루어질 수 있는가, 아니면 외부의 상황과 환경 변화가 그 과정에 필수적인가?', '인간은 완전히 독립적으로 죄에서 벗어날 수 있는가, 아니면 사회와 타인의 힘이 필요한가?', '자기 자신을 구원하기 위해 무엇이 가장 중요한가? 이것은 개인의 의지와 행동에 달려있는가, 아니면 외부의 도움과 지원에 달려있는가?']"}
]

# getAnswer_prompt = [
#     {"role" : "system",
#      "content" : "토론의 대상 두명이 소설속에서 대립하는 인물이고, 주제 역시 이러한 대립을 의도한 질문이야. 두 인물 각각의 의견, 근거를 표현해서 \
#          {'answer1':{\
#             'answer' : '',\
#             'role' : ''\
#         },\
#         'answer2':{\
#             'answer' : '',\
#             'reason' : '',\
#             'role' : ''\
#         } \
#     }의 형식으로 말해줘. 말 할 때 앞부분에 다른 사람의 이름을 호명하는 부분은 쓰지 마"},
    
#     {"role" : "user",
#     "content" : "소설 '돈키호테'에서 대립하는 '돈키호테'와 '산초판자' 두 인물이 '이상주의는 아름다운 생각일 수 있지만, 그것이 현실에서 어떻게 구현될 수 있는가? 혹은 이상주의는 결국은 불가능한 목표나 현실성 없는 계획을 세우는 것이 아닌가?'라는 산초판자의 질문에 돈키호테 입장에서 대답할 수 있는 답변 1개,산초판자 입장에서 대답할 수 있는 답변 1개를 각각 알려줘"},
#     {"role" : "assistant",
#      "content" : "{'answer1':{'answer' : '이상주의는 마치 바람에 날리는 불꽃과 같다; 가끔은 사라져 보이지만, 그 불꽃이 우리에게 빛과 힘을 주는 것이다. 이상주의는 단순히 현실을 바꿀 수 있는 큰 힘이라고 생각한다. 그것이 있어야만 새로운 시대와 변화가 시작된다.','reason' : '이상주의가 큰 변화와 혁명을 주도하는 힘이 될 수 있다는 점을 역사적 예시로 밝힌다. 프랑스 혁명, 미국 독립전쟁 등은 이상의 힘으로 세상을 바꾼 예이다. 따라서 이상주의는 단순한 아름다운 생각 이상의 가치가 있다고 주장한다.','role' : '돈키호테'},'answer2':{'answer' : '이상주의가 높은 곳을 향하게 하는 건 인정하지만, 두 발이 땅에 닿지 않으면 결국은 넘어진다. 실용주의는 현실적인 한계와 대처 방안을 제시해주며, 이상을 실현 가능한 단계로 구체화하는 데 도움을 준다.','reason' : '실용주의는 현실적인 문제 해결을 중시하며, 이상을 추구하는 것도 중요하지만 그것을 실현하기 위한 실질적인 방법이 필요하다고 주장한다. 예를 들면, 복지나 교육과 같은 사회 문제를 해결하는 데 있어 이상만을 추구할 경우, 구체적인 계획이 없으면 아무런 변화를 가져오지 못할 것이다. 따라서 실용주의는 이상주의를 현실로 만드는 구체적인 방법을 제공한다고 볼 수 있다.','role' : '산초판자'} }"},
    
# ]
getAnswer_prompt = [
    {"role" : "system",
     "content" : "토론의 대상 두명이 소설속에서 대립하는 인물이고, 주제 역시 이러한 대립을 의도한 질문이야. 두 인물 각각의 의견을 \
         {'answer1':{\
            'answer' : '',\
            'role' : ''\
        },\
        'answer2':{\
            'answer' : '',\
            'role' : ''\
        } \
    }의 형식으로 말해줘. 말 할 때 앞부분에 다른 사람의 이름을 호명하는 부분은 쓰지 마"},
    
    {"role" : "user",
    "content" : "소설 '돈키호테'에서 대립하는 '돈키호테'와 '산초판자' 두 인물이 '이상주의는 아름다운 생각일 수 있지만, 그것이 현실에서 어떻게 구현될 수 있는가? 혹은 이상주의는 결국은 불가능한 목표나 현실성 없는 계획을 세우는 것이 아닌가?'라는 산초판자의 질문에 돈키호테 입장에서 대답할 수 있는 답변 1개,산초판자 입장에서 대답할 수 있는 답변 1개를 각각 알려줘"},
    {"role" : "assistant",
     "content" : "{'answer1':{'answer' : '이상주의는 마치 바람에 날리는 불꽃과 같다; 가끔은 사라져 보이지만, 그 불꽃이 우리에게 빛과 힘을 주는 것이다. 이상주의는 단순히 현실을 바꿀 수 있는 큰 힘이라고 생각한다. 그것이 있어야만 새로운 시대와 변화가 시작된다.','role' : '돈키호테'},'answer2':{'answer' : '이상주의가 높은 곳을 향하게 하는 건 인정하지만, 두 발이 땅에 닿지 않으면 결국은 넘어진다. 실용주의는 현실적인 한계와 대처 방안을 제시해주며, 이상을 실현 가능한 단계로 구체화하는 데 도움을 준다.','role' : '산초판자'} }"},
    
]


getFeedback_prompt = [
    {"role" : "system",
     "content" : "토론 중 답변에 대한 피드백을 주는 부분이야. \
         답변의 형식을, '저는 ~~~에는 동의하지만, ~~~에 있어서는 ~~~한 입장입니다.'에서 ~~~를 채워줬으면 좋겠어."},
 
    {"role" : "user",
    "content" : "소설 '돈키호테'를 주제로 '돈키호테'와 '산초판자가'  가상의 독서토론을 나누고 있어.\
        '이상주의는 아름다운 생각일 수 있지만, 그것이 현실에서 어떻게 구현될 수 있는가? 혹은 이상주의는 결국은 불가능한 목표나 현실성 없는 계획을 세우는 것이 아닌가?'라는 산초 판자의 질문에\
        '이상주의는 마치 바람에 날리는 불꽃과 같다; 가끔은 사라져 보이지만, 그 불꽃이 우리에게 빛과 힘을 주는 것이다. 이상주의는 단순히 현실을 바꿀 수 있는 큰 힘이라고 생각한다. 그것이 있어야만 새로운 시대와 변화가 시작된다.'\
        라고 돈키호테가 답변을 했어.\
        돈키호테의 답변에대한 산초판자의 피드백을 부탁해"},
     {"role" : "assistant",
     "content" : "저는 '이상주의가 새로운 시대와 변화의 시작을 위해 필요하다'는 부분에는 동의합니다. 그러나 '이상주의가 단순히 현실을 바꿀 수 있는 큰 힘이라고 생각한다'는 부분에 있어서는 '실용적인 접근 방식이 없으면 이상주의는 단순한 환상에 불과하다'는 의견입니다."},

    
]

getScore_prompt = [
    {"role" : "system",
     "content" : "유사도 질문에 대한 답변은 숫자로만 딱 알려줘. 그리고 한문장으로 요약하는건 한줄로 해줘.\
         {'score' : '유사도 점수',\
         'result' : '한줄 요약'} 이 형식으로 데이터를 줘."},

    {"role" : "user",
    "content" : "'파우스트'라는 소설에을 주제로 '파우스트'와 '메피스토펠레스' 두 인물이 '헌신이 인생의 가치를 높이는가, 아니면 그것이 인생을 더 힘들게 만드는가?'라는 주제로 가상 토론을 하고있어.\
            '파우스트'가 1. '헌신은 결국 사람을 성장시키는 힘이다. 어떤 일에 헌신하는 것은 그 일을 통해 배우게 되며, 그 과정에서 자신이 성장하게 된다.'\
                2. '정신적인 만족이 더 가치있다. 헌신은 우리가 무엇을 위해 살아가는지, 어떤 목표를 향해 나아가는지를 정의하는 것이다. 물질적인 만족은 일시적이고 허상일 수 있지만, 정신적인 만족은 영원하다.'\
                3. '헌신은 우리가 추구하는 이상을 향한 동력이며, 자신을 희생하는 것이 아니라 오히려 더 큰 성장과 발전을 위한 과정이라고 본다. 그것은 자기자신을 뛰어넘는 데 필요한 동력이다.'라는 주장을 내세웠을때, \
            이 3가지 주장이 소설속 '파우스트'의 사고 얼마나 유사할까? 또 위 3가지의 주장들을 한문장으로 요약해줘."},
    {"role" : "assistant",
     "content" : "{'score' : 80, 'result':'파우스트는 헌신을 통한 성장, 정신적 만족, 그리고 이상을 추구하는 동력으로 본다'}"}
    
]
#
        # 'agree' : '산초판자의 피드백에서 헌신이 과도하면 부담과 압박으로 이어질 수 있다는 점은, 헌신의 양면성을 잘 지적한 것 같습니다.',\
         #'degree' : '다른 의견에 대한 요약'}
getSummary_prompt = [
    {"role" : "system",
     "content" : "피드백 요약은 한문장으로 해주고, \
         {'result' : ''} 이 형식으로 데이터를 줘."},
    
    {"role" : "user",
    "content" : "'파우스트'라는 소설을 주제로 '파우스트'와 '메피스토펠레스' 두 인물이 '헌신이 인생의 가치를 높이는가, 아니면 그것이 인생을 더 힘들게 만드는가?'라는 주제로 가상 토론을 하고있어.\
        매피스토펠레스가\
                1. '저는 '헌신이 사람을 성장시키는 힘이라'는 부분에는 동의하지만, '어떤 일에 헌신하는 것은 그 일을 통해 배우게 되며, 그 과정에서 자신이 성장하게 된다'는 부분에 있어서는 '헌신이 과도하면 오히려 부담과 압박으로 이어질 수 있으며, 그로 인해 개인의 성장을 방해할 수 있다'는 입장입니다.'\
                2. '저는 '헌신이 우리가 무엇을 위해 살아가는지, 어떤 목표를 향해 나아가는지를 정의하는 것'이라는 부분에는 동의합니다. 그러나 '물질적인 만족은 일시적이고 허상일 수 있지만, 정신적인 만족은 영원하다'는 부분에 있어서는 '물질적 만족도 개인의 삶에 중요한 역할을 할 수 있으며, 항상 허상이라고 단정짓기 어렵다'는 입장입니다.'\
                3. '저는 '헌신이 우리가 추구하는 이상을 향한 동력이며, 자신을 희생하는 것이 아니라 오히려 더 큰 성장과 발전을 위한 과정'이라는 부분에는 동의합니다. 그러나 '헌신은 자기자신을 뛰어넘는 데 필요한 동력'이라는 부분에 있어서는 '헌신이 과도하게 요구될 경우, 개인의 행복과 삶의 질을 저해할 수 있다'는 의견입니다.'라는 3가지의 의견을 내놨을때, 이 피드백을 한문장으로 요약해줘."},
    {"role" : "assistant",
     "content" : "{'result' : '메피스토펠레스는 헌신이 일정 수준에서는 성장, 목표 설정, 그리고 이상을 추구하는 데 도움이 될 수 있다고 동의하지만, 과도한 헌신은 오히려 부담과 압박을 생성하며, 물질적 만족 또한 무시할 수 없다고 주장합니다.'}"}
    
]
# getAnswer_prompt = [
#     {"role": "system",
#      "content": "The two subjects of the discussion are opposing characters in a novel, and the topic is also a question intended to highlight such opposition. Express the opinions and rationale of each character in the format \
#          {'answer1': {\
#             'answer': '',\
#             'reason': '',\
#             'role': ''\
#         },\
#         'answer2': {\
#             'answer': '',\
#             'reason': '',\
#             'role': ''\
#         }\
#     }. When speaking, omit the part where you call out the other person's name."},
    
#     {"role": "user",
#      "content": "In the novel 'Don Quixote,' provide one answer each from the perspectives of 'Don Quixote' and 'Sancho Panza' to Sancho Panza's question, 'Can idealism be a beautiful thought but how can it be implemented in reality? Or is idealism ultimately setting unachievable goals or unrealistic plans?'"},
     
#     {"role": "assistant",
#      "content": "\
#         {\
#             'answer1': {\
#                 'answer': 'Idealism is like a flame blown by the wind; it may sometimes disappear, but it is that flame that gives us light and strength. I see idealism as a powerful force that can change reality. It is what initiates new eras and transformations.',\
#                 'reason': 'Highlights the role of idealism as a driving force behind major changes and revolutions, citing historical examples such as the French Revolution and the American Revolutionary War. Therefore, argues that idealism has a value beyond being a mere beautiful thought.',\
#                 'role': 'Don Quixote'\
#             },\
#             'answer2': {\
#                 'answer': 'While idealism may point us upward, if our feet are not on the ground, we will eventually fall. Pragmatism provides realistic limitations and solutions, helping to make ideals feasible.',\
#                 'reason': 'Emphasizes the importance of practical problem-solving, arguing that while pursuing ideals is important, concrete methods are necessary for realization. For instance, without a practical approach, ideals alone cannot bring about any change in social issues like welfare and education.',\
#                 'role': 'Sancho Panza'\
#             }\
#         }"},
    
#     {"role": "user",
#      "content": "In the novel 'Faust,' provide one answer each from the perspectives of 'Mephistopheles' and 'Faust' to Faust's question, 'Are ethical standards determined by natural law, or are they formed by society and culture?'"},
    
#     {"role": "assistant",
#      "content": "\
#         {\
#             'answer1': {\
#                 'answer': 'Ethical standards should continuously evolve and change through individual exploration and self-development. Rules fixed by natural law or by society and culture only limit human advancement.',\
#                 'reason': 'Faust has an insatiable desire for knowledge and human capability, even making a deal with the devil to satisfy this. From his perspective, if ethical standards are determined by fixed rules, it restricts human freedom and growth. Faust believes that the process of finding ethical truth through personal experience and knowledge is crucial.',\
#                 'role': 'Faust'\
#             },\
#             'answer2': {\
#                 'answer': 'Ethical standards are formed by society and culture and are relative and subject to change. Ultimately, everything is governed by rules of power and cunning.',\
#                 'reason': 'Mephistopheles, being a devil, knows human weaknesses and instincts well. He often mocks the ethical standards set by society and culture, arguing that they are often influenced by power and gain. According to him, ethical standards are just human-made rules and do not possess intrinsic value.',\
#                 'role': 'Mephistopheles'\
#             }\
#         }"} 
# ]




