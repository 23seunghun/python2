'''
    202395020 신승훈
    p.169 6.5 섭씨온도 구하기
'''


def cel2fah(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    for celsius in range(0, 51, 10):
        fahrenheit = cel2fah(celsius)
        print(f"{celsius}도에 해당하는 화씨 온도는 {fahrenheit}도 입니다.")

if __name__ == "__main__":
    main()
