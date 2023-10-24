'''
    202395020 신승훈
    p.169 6.6 판단하는 함수
'''

def is_prime(n):
    if n <= 1:  # 1또는1보다 작은 수는 소수가 아님.
        return False
    for i in range(2, int(n**0.5) + 1):  #n의 제곱근까지만 확인
        if n % i == 0:
            return False
    return True

# 사용자 입력을 받아서 소수인지 아닌지 판단.
num = int(input("소수 검사를 할 정수를 입력하시오 : "))
if is_prime(num):
    print(f"{num}은(는) 소수입니다.")
else:
    print(f"{num}은(는) 소수가 아닙니다.")
