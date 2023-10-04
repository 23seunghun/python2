'''
    작성일 : 2023.10.04
    작성자 : 202395020 신승훈 컴퓨터공학부
    설명 : 조건에 따라 반복하는 while 문
            교재 127 페이지

'''
#while 조건식 : => : 반드시 사용.
#   들여쓰기로 반복하면서 할일 작성.
# 반복문에서는 반드시 종료 조건이 있어야 한다.

under_construction = True #공사중.

while under_construction :
    response =  input("공사가 완료 되었습니까?")
    if response == "예" :
        under_construction = False #공사 완료의 의미
        
print("루프를 탈출했습니다.")