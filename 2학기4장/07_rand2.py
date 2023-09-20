'''
작성일 : 2023.09.20
    작성자 : 컴공과 202395020 신승훈 
    설명 : 선택문 if~else
            random 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 =>
            1 =>
            2 =>
            두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''

import random

print("::가위 바위 보 게임 시작. ::")
player1= input("Player1의 이름 : ")
player2= input("Player2의 이름 : ")

num1= random.randrange(3) #plyer 1 의 랜덤 수
num2= random.randrange(3) #plyer 2 의 랜덤 수

# plyer 1의 가위바위보 출력 
print(player1, " : ", end='')
if num1 == 0:
    print("가위")
elif num1 == 1:
    print("바위")
if num1 == 2:
    print("보")

# plyer 2의 가위바위보 출력 
print(player2, " : ", end='')
if num2 == 1:
    print("가위")
elif num2 == 2:
    print("바위")
else:
    print("보")

# 승자 제출
if num1 == num2:
    print("무승부!")
elif (num1 == 0 and num2 == 2) or (num1 == 1 and num2 == 0) or (num1 == 2 and num2 == 1):
    print(player1, "가 이겼습니다!")
else:
    print(player2, "가 이겼습니다!")
