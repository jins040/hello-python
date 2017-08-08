# 함수 - 리뷰 연습문제, main 활용


def shut_down(s):
    if s == 'yes':
        return 'Shutting down'
    elif s == 'no':
        return 'Shutdown aborted'
    else:
        return 'Sorry'


def distance_from_zero(param):
    if type(param) == int or type(param) == float:
        return abs(param)
    else:
        return 'Nope'


def main():
    print(shut_down('yes'))

    import math
    print(math.sqrt(16))

    print(distance_from_zero('String'))

main()
