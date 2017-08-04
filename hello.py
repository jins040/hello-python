"""
파이썬은 내부적으로 객체를 재사용한다.
"""
x = 5
print(id(x))

y = 100
print(id(y))
y = 5
print(id(y))

# # int -> str
# e = str('hi' + 25)
# print(e)  # : 에러(string과 int 연산 시 자동 변화 X)

# # String -> int
# i = int("hello")
# print(i)    #: hello를 int로 바꿀 수 없어 에러

# 문자열 자르기
a_mystr = 'it\'s very hot today!'
print(a_mystr)
print(a_mystr[5:9])

# 인덱스를 카운트하기 힘들 때는 -index도 가능
print(a_mystr[-6:])
print(a_mystr[-10:-7])

"""list와 인덱스"""
# list&index
color = ['black', 'white', 'blue', 'grey', 'purple']
print(color[0])
print(color[2])
print(color[4])

# 값 삭제
color.remove('black')
print(color)

# 인덱스 삭제
del color[2]
print(color)


# 값 추가(중간에 끼워넣기)
color.insert(0, 'silver')
print(color)

# 값 수정, append(data) 함수로 데이터 마지막에 추가
color.append('gold')
print(color)

# 값 수정, 인덱스 바꾸기
color[2] = '블루'
print(color)

# 리스트와 리스트를 합치기
other_colors = ['royal blue', 'sky blue']
color = color + other_colors
print(color)

# 리스트에서 가장 큰 숫자 찾기
ft = [3, 1, 5, 6, 10, 2, 4, 8, 7, 5, 9]
ft.sort(reverse=True)
print(ft)
print(ft[0])

# 튜플 사용해보기(List와 비교)
a_tuple = ('red', 'blue')
c, d = a_tuple
print(c)
print(d)
other_tuple = 'red', 'blue'
print(other_tuple[1])
print(other_tuple[-2])

