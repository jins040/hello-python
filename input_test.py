# input() built-in function

from_user = input('글자를 입력하시고 엔터를 치세요 : ')

print(from_user)    # 입력을 받을 수 있도록

# Ex) 간단한 단어 번역기 만들기
postfix = 'ay'

input_word = input('단어를 입력해주세요 : ')

if len(input_word) > 0 and input_word.isalpha():        # .isalpha 는 글자인지를 판별해주는 method
    word = input_word.lower()                           # .lower 는 소문자로 바꿔주는 method
    first_chr = word[0]
    result = word[1:len(word)] + first_chr + postfix
    print(result)
else:
    print('invalid word...')