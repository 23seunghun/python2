'''
    202395020 신승훈
    p.143 5.7 암스트롱
'''


def armstrong():
    num1 = []
    for x in range(1, 10):
        for y in range(0, 10):
            for z in range(0, 10):
                number = x * 100 + y * 10 + z
                if number == x**3 + y**3 + z**3:
                    num1.append(number)
    return num1


num1 = armstrong()
print("세 자리 암스트롱 수는 : ")
for number in num1:
    print(number)

