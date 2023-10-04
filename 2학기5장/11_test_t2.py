
'''
    작성일 : 2023.10.04
    작성자 : 202395020 신승훈 컴퓨터공학부
    설명 : 사용자가 입력하는 숫자의 합을 계산

    문제 분석 : 사용자가 입력한 숫자를 더하며 사용자가 "yes"(yes or no)라고 답한 동안에만 결과 출력
    +이외의 답변을 하였을 떄 "다시 입력해 주세요로 출력하기"
    
    필요한 변수 : while
'''

total = 0  # 합계를 0으로 설정
ask = 'yes'  # ask를 yes로 설정

while ask == 'yes':
    score = input("숫자를 입력하시오 : ")
    if score.isdigit():  # 입력된 값이 숫자인지 확인

        score = int(score)
        total = total + score
        ask = input("계속 하시겠습니까?(yes/no):")
        while ask not in ['yes', 'no']:  # yes나 no 이외의 값이 입력되면 다시 입력 요청
            print("다시 입력해주세요.")
            ask = input("계속 하시겠습니까?(yes/no):")
    else:
        print("숫자를 입력해주세요.")

print('합계는 : ', total)
