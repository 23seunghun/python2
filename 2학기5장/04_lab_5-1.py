'''
작성일 : 2023.09.27
작성자 : 컴공과 202395020 신승훈
설명 : 터틀 그래픽으로 여러 개의 원을 그려보자
'''

import turtle as t

# 원 하나 그리기
# t.circle(100)

for count in range(10) :
    t.circle(100)
    t.left(360/10)

t.mainloop() #종료
#t.done ()# 종료