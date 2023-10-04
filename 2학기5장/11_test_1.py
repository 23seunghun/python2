'''
    작성일 : 2023.10.04
    작성자 : 202395020 신승훈 컴퓨터공학부
    설명 : 사용자가 입력하는 숫자의 합을 계산

    문제 분석 : 사용자가 입력한 숫자를 더하며 사용자가 "yes"(yes or no)라고 답한 동안에만 결과 출력
    
    필요한 변수 : while
'''

total = 0 #합계를 0으로 설정
ask ='yes' #ask 를 yes로 설정

while ask == 'yes': # ""
    score = int(input("숫자를 입력하시오 : ")) #숫자를 입력받고
    total = total + score #숫자를 total 더한다.
    ask = input("계속 하시겠습니까?(yes/no):") #ask 가 yes 로 입력받으면 반복한다

print('합계는 : ',total ) #합계 값을 제출

