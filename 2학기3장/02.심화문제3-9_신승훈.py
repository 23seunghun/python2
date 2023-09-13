'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터 공학과 202395020 신승후 
    설명 : 98페이지 문제 3.9
            평균시속과 이동시간을 입력받아
            이동 시간은 시,분,초 단위로 출력하고,
            이동한 거리를 계산하여 출력하시오.
'''

speed = float(input("평균 시속(km/h)을 입력하세요: "))
hours = int(input("이동 시간(h)을 입력하세요: "))

minutes = int(input("이동 시간(분)을 입력하세요: "))
seconds = int(input("이동 시간(초)을 입력하세요: "))

total = (hours * 3600) + (minutes * 60) + seconds

distance = speed * (total / 3600)

print("이동 시간: {}시 {}분 {}초". format(hours,minutes,seconds))
print("이동한 거리: {} km". format (distance))



