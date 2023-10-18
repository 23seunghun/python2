'''
    작성일 : 2023.10.18
    작성자 : 컴공과 202395020 신승훈
    설명 : 리스트 객체 생성과 참조
'''

fruits1=['딸기','수박','바나나']


# 실제 값을 복사하는게 아니라 리스트의 저장 위치(주소)가 복사된다.
fruits2 = fruits1
print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)


fruits2[1] = '망고' #후르츠2의 [1]번지 과일을 망고로 바꾸면..

print("fruits1 : ", fruits1) #모두 1번지 내용이 망고로 바꾼다
print("fruits2 : ", fruits2) #주소를 창조하기 때문(같은 주소)

#주소 확인=> 메모리 위치 정보 알아보기 id()함수
print("fruits1의 id : ", id(fruits1)) 
print("fruits2의 id : ", id(fruits2)) #두 리스트의 id정보가 같다

'''
    리스트 내용 복제하기 list(함수)
'''

fruits2 = list(fruits1) #내용 복제(배정)
print("::내용 복제 후 1::")
print("fruits1의 id : ", id(fruits1)) 
print("fruits2의 id : ", id(fruits2)) #두 리스트의 id정보가 같다

#내용 복제2
fruits3=fruits1[:]
print("::내용 복제 후2::")
print("fruits1:",fruits1)
print("fruits3:",fruits3)

print("fruits1의 id : ", id(fruits1)) # id정보가 다르다
print("fruits3의 id : ", id(fruits3))

fruits3[0]='수박' #0번지 내용을 수박으로 바꾼다
print("::fruits3의 0번지에 수박으로 내용 바꾼 후::")
print("fruits1:",fruits1)
print("fruits3:",fruits3)




