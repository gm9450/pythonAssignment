# 숫자 맞추기 게임

# ---수정사항---
# 횟수 제한 추가
# 난이도 추가(6회, 8회, 10회)

import random
import time

tries = 0
guess = 0
answer = random.randint(1, 100)
tries_limit = 0

print("1부터 100까지의 숫자중 하나를 맞추는 게임입니다.")

difficulty = int(input("1 : 쉬움(10회)\n2 : 보통(8회)\n3 : 어려움(6회)\n입력 : "))
if (difficulty == 1):
    tries_limit = 10
    print("쉬움!")
elif (difficulty == 2):
    tries_limit = 8
    print("보통!")
elif (difficulty == 3):
    tries_limit = 6
    print("어려움!")

while (tries <= tries_limit):
    guess = int(input("숫자 입력 : "))
    tries += 1
    if(guess == answer):
        break
    elif (guess > answer):
        print("다운!")
    elif (guess < answer):
        print("업!")

if (tries > 10):
    print("10회 이상 틀림")
    print("정답 :", answer)
else:
    print("정답! 시도횟수 :", tries)
