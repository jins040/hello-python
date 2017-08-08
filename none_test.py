# None == false

mp_director_dic = {'봉준호': '옥자',
               '제임스 카메론': '타이타닉',
               '마틴 스콜세지': '카지노',
               '크리스토퍼 놀란': '인셉션',
               '박찬욱': '올드보이'}

masterpiece = mp_director_dic.get('유승완')

print(type(mp_director_dic))

print(masterpiece)
print(type(masterpiece))

if masterpiece:
    print('유승완 감독의 대표작은 ', masterpiece, '입니다.')
else:
    print('유승완 감독의 데이터가 없습니다.')
