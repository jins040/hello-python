# 영화 감독과 대표작을 데이터로 표현
# 1. 리스트 2개
# 2. 이중 리스트(이차원 리스트), list of list, two dimension list

director = ['봉준호', '제임스 카메론', '마틴 스콜세지', '크리스토퍼 놀란', '박찬욱']
masterpiece = ['옥자', '타이타닉', '카지노', '인셉션', '올드보이']

mp_director = [['봉준호', '옥자'],
               ['제임스 카메론', '타이타닉'],
               ['마틴 스콜세지', '카지노'],
               ['크리스토퍼 놀란', '인셉션'],
               ['박찬욱', '올드보이']]

# Dictionary 타입
# mp_director_dic = {}                                  # dictionary 초기화
mp_director_dic = {'봉준호': '옥자'}                     # key: value로 구분
mp_director_dic.setdefault(director[1], masterpiece[1]) # setdefault는 key값이 기존에 있으면 추가 X
mp_director_dic.setdefault(director[2], masterpiece[2])
mp_director_dic.setdefault(director[3], masterpiece[3])
if '박찬욱' not in mp_director_dic:
    mp_director_dic['박찬욱'] = '올드보이'

print(mp_director_dic.get('봉준호'))
print(mp_director_dic)

del mp_director_dic['박찬욱']

print(mp_director_dic)
