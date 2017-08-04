# 문장 속에 나타나는 문자 갯수를 카운팅해서 딕셔너리 형태로 표현

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
word_count = {}

for e in message:
    if e not in word_count:
        word_count.setdefault(e, 1)
    else:
        word_count[e] = word_count.get(e) + 1

print(word_count)
