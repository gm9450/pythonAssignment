# 가위바위보 게임(동전던지기 게임)

# ---수정사항---
# 1,2로 시작과 종료를 할수 있음
# 가위바위보 게임으로 변경
# 가위(0) > 보(2) > 바위(1) > 가위(0)
# 가위바위보를 숫자로 변환하는 함수
# 숫자를 가위바위보 글자로 변환하는 함수
# 컴퓨터와 사람의 승패를 판단하는 함수
# 승패에 따라 문장을 출력해주는 함수

import random

# 글자를 숫자로 변경 ex)가위 -> 0
def RPS(n):
    if (n == '가위'):
        return 0
    elif (n == '바위'):
        return 1
    elif (n == '보'):
        return 2
    else:
        return 3

# 숫자를 글자로 변경 0 -> 가위
def URPS(n):
    if (n == 0):
        return '가위'
    elif (n == 1):
        return '바위'
    elif (n == 2):
        return '보'
    else:
        return "잘못됨"

# a1는 컴퓨터, a2는 사람
# 승패를 판단함
def RPS_j(a1, a2):
    if (a1 == 0):
        if (a2 == 0):
            return 'tie'
        elif (a2 == 1):
            return 'win'
        else:
            return 'defeat'
    elif (a1 == 1):
        if (a2 == 0):
            return 'defeat'
        elif (a2 == 1):
            return 'tie'
        else:
            return 'win'
    elif (a1 == 2):
        if (a2 == 0):
            return 'win'
        elif (a2 == 1):
            return 'defeat'
        else:
            return 'tie'

# 결과 출력
def j_p(n):
    if (n == 'win'):
        print("당신이 이겼습니다.")
    elif(n == 'defeat'):
        print("당신이 졌습니다.")
    elif (n == 'tie'):
        print("서로 비겼습니다.")
       

while True:
    print("----------------")
    print("가위바위보 게임")
    print("1 : 시작\n2 : 종료")
    print("----------------")
    command = int(input("명령어를 입력해주세요. : "))
    if (command == 1) :
        a1 = random.randrange(3)
        while True:
            a2 = input("무엇을 낼까요? : ")
            a2 = RPS(a2)
            if (a2 < 3):
                break
            print("잘못 된 값이에요.")
        print("----------------")
        print("컴퓨터 :", URPS(a1))
        print("사람 :", URPS(a2))
        j_p(RPS_j(a1, a2))
        print("----------------\n")
    elif (command == 2) :
        break
    else :
        print("제대로 입력해주세요.")