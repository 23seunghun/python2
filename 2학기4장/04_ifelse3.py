'''
    작성일 : 2023.09.20
    작성자 : 컴공과 202395020 신승훈 
    설명 : 선택문 if~else
            교통카드의 종류로 '청소년','성인' 카드가 있다고 하자.
            사용자에게 카드의 종류를 입력받아 청소년이면 '청소년입니다'
            '성인' 이면 '성인입니다'.를 출력하자
'''
# 1.카드 종류를 입력받는다.
card = input("카드를 종류를 입력하시오('청소년','성인'중 하나 입력) :")

# 2. 입력받은 카드 종류가 청소년인지 성인인지 판단한다.
if card =='성인' :
    print("성인입니다.")
if card =='청소년' :
    print("청소년입니다.")
else:
    print("다시 입력해 주세요.")


    