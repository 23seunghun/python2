'''
    작성일 : 2023.10.11
    작성자 : 컴공과 202395020 신승훈
    설명 : lab 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.

    리스트에 10개인 값을 랜덤으로 생성하고,
    max또는 min을 입력 받아 최대,최소값을 찾아 돌려주는 함수
    

    (함수)
            5). 두 값을 전달받아 매개 변수에 저장.
            6). 최대값, 최소값을 찾는다.
            7). 값을 돌려준다.
    (메인)
        1.무한반복
            1). 렌덤으로 10~99까지 10개의 수를 리스트로 생성
            2). 생성된 리스트를 출력
            3). 사용자로부터 최대값을 알고 싶은지 최솟값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4). 입력받은 max 또는 min 과 생성된 리스트를 가지고 함수 호출
            8). 돌려 받은 최대값 또는 최솟값을 출력한다.
            
'''

import random

# 함수: 리스트에서 최대값 또는 최소값을 찾아 반환
def find_max_or_min(arr, choice):
    result = arr[0]  

    for num in arr:
        if choice == "max" and num > result:
            result = num  # 최대값 찾기
        elif choice == "min" and num < result:
            result = num  # 최소값 찾기

    return result

while True:  
    numbers = [random.randint(10, 99) for _ in range(10)]  

    print("생성된 숫자 리스트:", numbers)

    choice = input("최대값 또는 최소값 입력 (max 또는 min 입력): ")

    if choice == "max" or choice == "min":
        result = find_max_or_min(numbers, choice)
        print(f"{choice} 값: {result}")
    else:
        print("다시 입력해 주세요. 'max' 또는 'min' 중 하나를 입력하세요.")
