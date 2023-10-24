'''
    202395020 신승훈
    p.195 7.2 for 루프를 사용하여 list 원소 계산
'''
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for i in list1:
    for j in list2:
        result = i * j
        print(f"{i} * {j} = {result}")
