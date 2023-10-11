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

def getMinMax(my_list, method='max'):
    if method == 'max' :
        maxValue = max(my_list)
        return '최대값 : ' , maxValue
    elif method == 'min' :
        minValue = min(my_list)
        return '최소값 : ' , minValue
    else :
       print('illegal method')
       
while(True):                
    # "_" 변수의 이름을 특별히 지정하지 않고, 단순히 반복 횟수를 나타내는 용도로 사용
    list_data = [random.randint(10, 99) for _ in range(10)]  # 10개의 랜덤 숫자를 가진 리스트 생성
    print('생성된 리스트 : ', list_data)
    
    input_result = input('최대값을 원하면 max, 최소값을 원하면 min을 입력하시오: ')
    print(getMinMax(list_data, input_result))