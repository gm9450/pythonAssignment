# 로그인 프로그램

# ---수정사항---
# 3번 틀릴시 10초, 6번 틀릴시 15초, 9번 틀릴시 입력 못함

import time

def penalty(n):
    if (n == 3):
        print("-"*20)
        print("3번 틀렸습니다.")
        print("10초 기다려 주세요")
        print("-"*20)
        count(10)
    elif (n == 6):
        print("-"*20)
        print("6번 틀렸습니다.")
        print("15초 기다려주세요")
        print("-"*20)
        count(15)
    elif (n == 9):
        print("-"*20)
        print("9번 틀렸습니다.")
        print("-"*20)

def count(n):
    for i in range(n, 0, -1):
        print(f"{i}초 남았습니다.")
        time.sleep(1)

password_answer = "pythonisfun"
n = 0
key = 0
while key == 0:
    password = input("암호를 입력하시오. : ")
    if (password == password_answer):
        key = 1
    else:
        n += 1
        print("로그인 실패")
        penalty(n)
        if (n == 9):
            break
    
if (key == 1):
    print("-"*20)
    print("로그인 성공")
    print("-"*20)
else:
    print("-"*20)
    print("더이상 로그인 불가")
    print("-"*20)