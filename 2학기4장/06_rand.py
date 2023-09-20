'''
작성일 : 2023.09.20
    작성자 : 컴공과 202395020 신승훈 
    설명 : 선택문 if~else
            random 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 =>
            1 =>
            2 =>
'''

import random

print("::가위 바위 보 게임 시작. ::")

num= random.randrange(3) #랜덤으로 0,1,2 생성하여 변수에 저장

# 가위 바위 보 출력
if num == 1:
    print("가위")
elif num == 2:
    print("바위")
else:
    print("보")
