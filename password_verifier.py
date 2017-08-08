# 연습문제 : 패스워드 검증기


def password_verifier(password):
    if len(password) >= 8 and password.isalnum():
        return True
    else:
        return False


def main():
    while 1:
        input_password = input('PassWord를 입력해주세요 : ')
        if password_verifier(input_password):
            print(password_verifier(input_password), '정상적인 패스워드입니다.')
            break
        elif input_password == 'quit':
            print('종료되었습니다.')
            break
        else:
            print(password_verifier(input_password), '패스워드를 다시 입력해주세요.')

main()
