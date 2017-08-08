# Module test

import random
dice_number = random.randint(1, 6)
print('주사위 숫자는 : ', dice_number)

dice = [0, 0, 0, 0, 0, 0]
for i in range(10000):
    dice_num = random.randint(1, 6)
    dice[dice_num - 1] += 1

print(dice)
