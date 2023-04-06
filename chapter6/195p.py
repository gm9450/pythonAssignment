# 점치는 게임

import sys
import random

def lucky_day():
    m = random.randint(1, 12)
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        d = random.randint(1, 31)
        print(f"행운의 날은 {m}월 {d}일 입니다!")
    elif (m == 2):
        d = random.randint(1, 28)
        print(f"행운의 날은 {m}월 {d}일 입니다!")
    else:
        d = random.randint(1, 30)
        print(f"행운의 날은 {m}월 {d}일 입니다!")

def lucky_time():
    h = random.randint(1, 24)
    m = random.randint(1, 60)
    print(f"행운의 시간은 {h}시 {m}분 입니다!")

def dice(n):
    luck = random.randint(1, n)
    print(f"주사위의 숫자는 {luck} 입니다!")

while True:
    print("-"*20)
    print("1 : 행운의 날")
    print("2 : 행운의 시간")
    print("3 : 주사위 굴리기(24면체)")
    print("4 : 종료")
    print("-"*20)
    n = int(input("명령어를 입력해주세요. : "))
    print("-"*20)
    if (n == 1):
        lucky_day()
    elif (n == 2):
        lucky_time()
    elif (n == 3):
        print("-"*20)
        dice(24)
    elif (n == 4):
        sys.exit
    else:
        continue