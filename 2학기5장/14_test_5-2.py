'''
    작성일 : 2023.10.04
    작성자 : 202395020 신승훈 컴퓨터공학부
    설명 :  두 수를 입력 받아 
            1.두수 사이의 합계를 출력하기
            2.두 수 사이의 짝수의 합계 출력하기

            for 또는 while 문을 사용

            심하문제 5.2 141쪽
'''
#두 수 입력 받아서 합계 계산 > total num +1 num +2


#두 수를 입력 받기
num1 = int(input("첫 번째 수를 입력 : "))
num2 = int(input("두 번째 수를 입력 : "))

'''if num2 < num1:
    num1, num2 = num2, num1'''
min_num =min(num1,num2) #큰 수
max_num =max(num1,num2) #작은 수 로 입력

#1번 문제. 1번 문제인 합계를 계산 
total = 0

while min_num <= max_num:
    total += min_num
    min_num += 1



#2번 문제: 2번 문제인 두 수 사이의 짝수의 합계 출력
score_total = 0

min_num = min(num1, num2)  # 작은 수를 다시 초기화

while min_num <= max_num:
    if min_num % 2 == 0:
        score_total += min_num
    min_num += 1

#결과
print(f"{num1}와 {num2} 사이의 합계 : {total}")
print(f"{num1}와 {num2} 사이의 짝수의 합계 : {score_total}")

