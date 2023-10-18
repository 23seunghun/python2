'''
    작성일 : 2023.10.18
    작성자 : 컴공과 202395020 신승훈
    설명 : 도시의 인구 자료에 대한 슬라이싱 하기.

    population=["서울",9765,"부산",3441,"인천",2954]
    1).이 러스트에서 서울의 인구인 두 번째 요소를 출력
    2).이 러스트에서 마지막 요소인 인천의 인구를 출력, 이때,음수로 된 인덱스를 사용
    3).각 도시의 이름을 step 값을 이용하여 출력
    4).각 도시의 인구를 step 값을 이용하여 출력한 후 이 값들의 합을 출력.
    

'''

population = ["서울", 9765, "부산", 3441, "인천", 2954]

# 서울의 인구 수를 구하기
seoul_population = population[1]
print(f"서울 인구: {seoul_population}")

# 마지막 요소로부터 인천의 인구 출력
incheon_population = population[-1]
print(f"인천 인구: {incheon_population}")

# step 값을 이용하여 도시 이름 출력
for i in range(0, len(population), 2):
    print(f"도시 리스트: {population[i]}")

# step 값을 이용하여 인구 출력 후 합 출력
populations = [population[i] for i in range(1, len(population), 2)]
population_sum = sum(populations)
print(f"인구의 합: {population_sum}")

