'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터 공학과 202395020 신승후 
    설명 : 피자의 면적을 구하시오
            피자의 반지름이 필요하다.
            피자의 반지름을 입력 받아 계산한다.
'''
# 1. 반지름을 입력 받아 변수에 저장. ->정수로 변환
r=int(input("파지의 반지름을 입력하시오 : "))
PI= 3.14 #3.14는 상수 -> 대문자로 변수 생성.

# 2.피자의 면적 계산
area = PI * r**2

# 3. 피자의 면적 출력
# 반지름이 00인 피자의 면적은 00.00 입니다.
print("반지름이 {}인 피자의 면적은 {:.2f}입니다.".format(r, area))





