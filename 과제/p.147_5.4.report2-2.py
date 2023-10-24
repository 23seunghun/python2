'''
    202395020 신승훈
    p.147_5.4 직각삼각형 별 도형 만들기
'''

def semo(height):
    for i in range(1, height + 1):
        print(i * "*")


try:
    num = int(input("숫자를 입력하세요 : "))
    semo(num)
except ValueError:
    print("다시 입력해 주세요.")
