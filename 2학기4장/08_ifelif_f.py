'''
작성일 : 2023.09.27
    작성자 : 컴공과 202395020 신승훈 
    설명 : 
'''


# 점수를 입력 받는다.
score = int(input("점수 입력 : "))


# 판단.
# 이 코드는 논리 오류가 발생한다. > 300점 입력하면 A학점으로 나온다.
print(":::첫 번쨰 성적 처리:::")

if score >= 90 :
    print("A학점")
elif score >= 80 :
    print("B학점")
elif score >=70 :
    print ("C학점")
elif score >=60 :
    print ("D학점")
else :
    print ("F학점")
#첫 번째 코드는 지정된 외의 점수 입력시 논리 오류 발생


print() #빈줄 출력

# 정확한 범위를 지정 > 성적의 범위를 벗어나면 잘못된 점수
'''
    90~100 A학점
    80~89 B학점
    70~79 C학점
    60~69 D학점
    0~59 F학점
'''
print(":::두 번쨰 성적 처리:::")
#지정된 이외의 점수를 입력시 else문으로 수정
if (90 <= score <= 100) :
    print("A학점")
elif (score >= 80 and score <=89) :
    print("B학점")
elif (70 <= score <= 79) :
    print("C학점")
elif (60 <= score <= 69) :
    print("D학점")
elif (0 <= score <= 59) :
    print("F학점")
else :
    print("점수를 잘못 입력하셨습니다.")

print()

# 점수는 무조건 0~100점 사이입니다. -아니면 잘못된 입력입니다. 
print(":::세 번쨰 성적 처리:::")
if 0 <= score <= 100 :
    if score >= 90 :
        print("A학점")
    elif score >= 80 :
        print("B학점")
    elif score >=70 :
        print ("C학점")
    elif score >=60 :
        print ("D학점")
    else :#A,B,C,D 학점이 아니면,
        print ("F학점")
else : # 0~100 사이의 점수가 아니면
    print("점수를 잘못 입력하셨습니다.")
        