import datetime

# 처음 날짜(이전)
y = int(input("년도를 입력해주세요 : "))
m = int(input("월을 입력해주세요 : "))
d = int(input("일을 입력해주세요 : "))
time_1 = datetime.date(y, m, d)
print(time_1, "입니다\n")

# 두번째 날짜(이후)
y = int(input("년도를 입력해주세요 : "))
m = int(input("월을 입력해주세요 : "))
d = int(input("일을 입력해주세요 : "))
time_2 = datetime.date(y, m, d)
print(time_2, "입니다\n")

# 두 날짜간의 차이 구하기
delta = time_1 - time_2
print(delta.days, "일이 차이가 납니다.")