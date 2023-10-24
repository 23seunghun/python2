'''
    202395020 신승훈
    p.195 7.7 리스트 문제.
'''

fruit_list = ['banana', 'orange', 'kiwi', 'apple', 'melon']

# 최대 길이
max_length = max(len(fruit) for fruit in fruit_list)

# 동일한 길이의 저장
to_remove = []

# 최대 길이의 문자열을 삭제할 문자열로 추가
for fruit in fruit_list:
    if len(fruit) == max_length:
        to_remove.append(fruit)

# 삭제 수행
for fruit in to_remove:
    fruit_list.remove(fruit)

# 결과 출력
print(f"가장 길이가 긴 문자열: {max(to_remove, key=len)}")
print(f"변경된 리스트: {fruit_list}")
