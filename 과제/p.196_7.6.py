'''
    202395020 신승훈
    p.195 7.6 for 루프를 사용하여 list 원소 계산
'''


def print_pyramid(input_string):
    length = len(input_string)
    for i in range(1, length + 1):
        print(input_string[:i].center(length + i - 1))

input_string = input("임의의 문자열을 입력하세요: ")
print_pyramid(input_string)
