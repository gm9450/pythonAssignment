# 초등생을 위한 산수 문제 발생기

# ---수정사항---
# 챕터7에 실습1 문제를 수정했음
# 램덤으로 3개의 대답중 선택해서 대답함
# 빼기, 곱하기 추가
# 곱하기에는 두번째 수가 한자리로 변경됨

import random

k = 'Y'
ga = 0      # 입력할 정답
answer = 0  # 진짜 정답
score = 0
while (k == 'Y'):
    for i in range(10):
        a = random.randrange(10, 100)
        c = random.randint(1, 3)
        if (c == 3):
            b = random.randrange(1, 10)
        else:
            b = random.randrange(1, 100)
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
            s1 = random.choice(["참 잘했어요!", "와! 대단해요!", "오오! 아주 잘하네요!"])
            print(s1)
            score += 1
            print(" ")
        else:
            s2 = s1 = random.choice(["아 아쉬워요!", "다음에는 더 잘할수 있어요!", "화이팅!"])
            print(s2)
            print(" ")

    print("-"*20)
    print(score, "문제 맞췄네요!")
    if (score >= 8):
        print("아주 잘하는데요?")
    elif (score < 8 and score >= 6):
        print("살짝 아쉽지만 괜찮아요!")
    elif (score < 6 ):
        print("같이 열심히 공부해봐요!")
    print("-"*20)
    k = input("다시해볼까요?(Y/N)")

print("그럼 다음에 봐요!")