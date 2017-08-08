# 여행 경비 계산 연습 문제


def hotel_cost(nights):
    return nights * 140


def flight_cost(city):
    if city == 'Cebu':
        return 483
    elif city == 'Singapore':
        return 620
    elif city == 'Bali':
        return 722
    elif city == 'Los Angeles':
        return 975
    else:
        return 0


def rental_car_cost(days):
    total_cost = days * 40
    if days >= 7:
        return total_cost - 50
    elif days >= 3:
        return total_cost - 20
    else:
        total_cost


def trip_cost(nights, city, rent_days, spending_money):
    return hotel_cost(nights) + flight_cost(city) + rental_car_cost(rent_days) + spending_money


def main():
    total_trip_cost = trip_cost(3, 'Cebu', 4, 1000)
    print('총 여행 비용은', total_trip_cost, '$ 입니다.')

main()
