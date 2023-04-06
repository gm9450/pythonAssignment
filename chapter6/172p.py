# 요리 타이머 작성하기

# ---수정사항---
# 10초 남았을때 울림

import time
import winsound

second = int(input("초단위의 시간 입력 : "))

for i in range(second, 0, -1):
    print(f"{i}초 남았습니다.")
    if ( i <= 10):
        print("벨 울림")
        winsound.Beep(300, 100)
    time.sleep(1)

winsound.Beep(400, 3000)
