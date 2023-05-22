# 수학 퀴즈 프로그램

#10개의 랜덤한 수학 문제 제시(프로그램을 실행할 때마다 다른 문제)
#문제 유형: 두 자리수 ± 한 자리수, 두 자리수 × 한 자리수
#한 문제 당 10점씩 계산하여, 사용자가 모든 문제에 대한 답을 입력한 후 점수를 화면에 출력
#마지막으로 “다시 하시겠습니까?(Y/N)”를 물음. 사용자가 Y를 입력하면 처음부터 다시 시작되고(무한 반복), 그렇지 않으면 “안녕히 가십시오!”를 출력하고 종료

# random모듈사용
# 문제 형식 : 두자리수 +-*/ 한자리수 형식
# 문제당 10점을 계산, 마지막 출력
# 반복 여부를 마지막에 확인

import random

k = 'Y'
ga = 0      # 입력할 정답
answer = 0  # 진짜 정답
score = 0
while (k == 'Y'):
    for i in range(10):
        a = random.randrange(10, 100)
        b = random.randrange(1, 10)
        c = random.randrange(1, 4)
        if (c == 1):
            print(a, "+", b, "= ", end='')
            ga = int(input())
            answer = a + b
        elif (c == 2):
            print(a, "-", b, "= ", end='')
            ga = int(input())
            answer = a - b
        elif (c == 3):
            print(a, "x", b, "= ", end='')
            ga = int(input())
            answer = a * b

        if (ga == answer):
            score += 10

    print("정수 =", score)
    k = input("다시하겠습니까?(Y/N)")

print("안녕히 가십시오!")