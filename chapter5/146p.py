# 닭이 우는 조건(종달새가 노래할까?)

# ---수정사항---
# 조건 : 닭이 수컷인가?
# 조건 : 빛을 감지했는가?
# 여름 3~4시에 운다.
# 겨울 5~6시에 운다
# 봄,가을 4~5시

import random
g = ["수탉", "암탉"]
i = random.randrange(2)
time = random.randint(1, 24)
season = random.randint(1, 12)
print("닭은", g[i],"입니다")
print("오늘은", str(season)+"월 입니다.")
print("지금 시각은", str(time)+"시 입니다.")
if (g[i] == "수탉"):
    if (season == 6 or season == 7 or season == 8):
        if (time == 3 or time == 4):
            print("닭이 웁니다.")
        elif (time > 4):
            print("닭은 3~4시에 이미 울었습니다.")
        else:
            print("닭이 아직 울지 않았습니다.")
    elif (season == 12 or season == 1 or season == 2):
        if (time == 5 or time == 6):
            print("닭이 웁니다.")
        elif (time > 6):
            print("닭은 5~6시에 이미 울었습니다.")
        else:
            print("닭이 아직 울지 않았습니다.")
    else:
        if (time == 4 or time == 5):
            print("닭이 웁니다.")
        elif (time > 5):
            print("닭은 4~5시에 이미 울었습니다.")
        else:
            print("닭이 아직 울지 않았습니다.")
else:
    print("암탉은 울지 않습니다.")