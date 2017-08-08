# for 문 test
colors = ['black', 'white', 'blue', 'grey', 'purple']

for color in colors:
    result = color[0].upper() + color[1:len(color)]
    print(result)

for e in range(3):
    print(colors[e])

# random
import random

for i in range(10):
    print(random.randint(1, 6))

for i in range(10):
    print(random.random())          # .random은 0~1 사이의 값

for i in range(10):
    print(random.choice([1, 2, 3, 4, 5, 6]))


# dictionary test : 3가지 방법으로 for 문 사용 가능
mp_director_dic = {'봉준호': '옥자',
               '제임스 카메론': '타이타닉',
               '마틴 스콜세지': '카지노',
               '크리스토퍼 놀란': '인셉션',
               '박찬욱': '올드보이'}

keys = mp_director_dic.keys()                      # 실제 내용은 List 타입
print(keys)
print('== for loop in dictionary using key ==')
for key in mp_director_dic.keys():
    print(mp_director_dic.get(key))

values = mp_director_dic.values()
print(values)
print('== for loop in dictionary using value ==')
for value in mp_director_dic.values():
    print(value)

take_all = mp_director_dic.items()                  # tuple 타입
print(take_all)
print('== for loop in dictionary using item ==')
for key, value in mp_director_dic.items():          # tuple unpacking
    print(key, value)
    print('%s in %s' % (key, value))

