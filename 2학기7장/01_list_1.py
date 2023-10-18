'''
    작성일 : 2023.10.18
    작성자 : 컴공과 202395020 신승훈
    설명 : 리스트 만들기
'''

#과일 리스트 만들기

fruits = ['딸기','사과','바나나']
print("과일 목록 : ", fruits)

#수박 추가 >> append() 메소드 사용

fruits.append('수박')
print("과일 목록(수박 추가):",fruits)
fruits.append('망고') 
print("과일 목록(망고 추가):",fruits)

#포도 추가 => +연산자 사용
fruits = fruits + ['포도'] #포도를 더해서 fruits 에 저장 >> num = num + 1 같은 의미
print("과일 목록(포도 추가):",fruits)

num = [1,2,3] + [4,5,6] #출력 결과=> 1,2,3,4,5,6
print("숫자 리스트 : ", num)


# 곱하기 * 연산자 => 1,2,3, 1,2,3, 1,2,3
num = [1,2,3] * 3
print("숫자 리스트 * 3 : ", num)

#in 연산자 => 포함되는가? True
print("과일 목록애 망고가 있나요?",'망고' in fruits) 


'''
    리스트의 원소 값을 자유롭게 조작해 보자.
'''
print()

print("과일 목록 : ",fruits)

#원하는 위치에 '두리안' 추가=> insert() 메소드
fruits.insert(3,'두리안')
print("과일 목록(3번지에 두리안 추가)")

#위치 찾기 => index()메소드
print("사과의 위치는?",fruits.index('사과'))

#사과 마지막에 추가
fruits.append('사과')
print("과일 목록(마지막에 사과 추가) : ",fruits)

#사과의 개수 =>count()메소드
print("사과의 개수는?",fruits.count('사과'))


'''
    리스트 항목 삭제
'''
print()

#사과 삭제 =>remove() 메소드
fruits.remove('사과')
print("과일 목록(사과 삭제 후) : ",fruits)

#항목 삭제 => pop() 메소드
fruits.pop()
print("과일 목록(마지막 과일 삭제): ",fruits)

#del() 키워드 =>포도 삭제
del fruits[0] #0번지 항목 삭제

print("과일 목록(포도(0번지)삭제):",fruits) 
