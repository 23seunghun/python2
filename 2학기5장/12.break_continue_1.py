'''
    작성일 : 2023.10.04
    작성자 : 202395020 신승훈 컴퓨터공학부
    설명 : 반복을 제어하는 break , continue
            교재 127페이지

    tost word = programming
'''

word = input("단어를 입력하세요 : ")

print(":: break ::")
for i in word :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        break
    else :
        print(i,end='') #결과 pr

print(":: break2 ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] : #모음을 만나면 반복 중지.
        break #반복을 중단한다. 반복을 빠져 나간다.
    else :
        print(i,end='') 

print()

print("::continue::")

for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] : 
        continue #반복의 처음으로 돌아간다. 아래 문장을 만날 수 있다.
    print(i,end='') #결과를 예상하십시오

