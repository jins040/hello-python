# 함수 만들기 연습

# Practice Makes Perfect


def cube(number):
    return number**3


def by_three(number):       # 함수끼리는 두 줄 간격이 convention
    if number % 3 == 0:
        return cube(number)
    else:
        return False


def main():
    print(cube(3))
    print(by_three(3))
    print(by_three(4))

main()
