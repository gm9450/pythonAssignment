# 카운트 다운 프로그램

# ---수정사항---
# 1~20초 사이의 수중 랜덤으로 선택
# 몇초를 세었는지 맞추는 게임

import time
import random

n = random.randint(1, 20)
print("1~20사이의 숫자만큼 초를 세겠습니다.")
print("시작")
for i in range(1, n+1):
    time.sleep(1)

print("끝")

s = int(input("몇초 일까요?"))
if not(n == s):
    print(n, "초입니다.")
    print(s-n, "초 차이가 나네요.")
else:
    print(n, "초입니다.")
    print("정답입니다!")