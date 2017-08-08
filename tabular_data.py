# 이중 루프를 활용하여 신문 배달을 하는 프로그램을 작성하세요
# 신문 구독료 미납된 세대에는 신문을 배달하지 않아야 합니다.
apart = [
    [101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]
    ]

not_payment = [101, 203, 301, 404]

for floor in apart:
    for house in floor:
        if house in not_payment:
            print(house, '호는 신문 구독료가 미납된 세대입니다.')
        else:
            print(house, '배달 완료')


# 함수를 통해 구현
print('== 함수를 통한 구현 ==')

def is_paid(h, np):
    """return boolean whether it is paid or not"""
    return h not in np

for floor in apart:
    for house in floor:
        if is_paid(house, not_payment):
            print("배달 완료")
        else:
            print("구독료 미납 세대")
