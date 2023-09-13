'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터 공학과 202395020 신승후 
    설명 : 터틀 만들기
'''




import turtle as t  #터틀 모듈을 사용하기 위한 준비
                    #turtle 클래스 객체를 t로 생성. (별명)

t.shape('turtle')
t.speed(2) 
# 선그리기
#t.forward(200)  # 200 픽셀 이동

# 삼각형 그리기
'''
t.forward(200) # 200픽셀만큼 이동
t.left(120) #왼쪽으로 120도 이동
t.forward(200) # 200픽셀만큼 이동
t.left(120) #왼쪽으로 120도 이동
t.forward(200) # 200픽셀만큼 이동
t.left(120) #왼쪽으로 120도 이동
'''

for i in range(10) :
    t.speed(10)
    t.forward(200) # 200픽셀만큼 이동
    t.left(120)#왼쪽으로 120도 이동

t.mainloop() # 그림판이 사라지지 않는다.

