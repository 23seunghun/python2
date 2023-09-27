'''
작성일 : 2023.09.27
작성자 : 컴공과 202395020 신승훈
설명 : 반복문 for 사용하기
'''

#본인 이름 5개 출력하기
print("::내 이름 5개 출력하기.::")
for i in range(5):
    print(i,":신승훈")


print("::내 이름 5개 출력하기.(리스트)::")
for i in [1,2,3,4,5]: #리스트
    print(i,":신승훈")


print("::리스트로 출력하는 19단 출력.::")
for num in[1,2,3,4,5,6,7,8,9] : #range(1,10)
    print(f"19 x {num} = {19*num}")


print("::문자열 내용 출력.::")
for i in "Hello" :
    print("i=", i ) # i값 출력


print("::bts 맴버 출력 (리스트)::")
bts=['V','J-Hope','Rm','Jk','jin','jimin','suga']

for i in bts:
    print(i)