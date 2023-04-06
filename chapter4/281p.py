import random
import statistics

n = int(input("몇번 반복할지 적어주셍 : "))
sample = []

# 1 부터 100 까지의 숫자를 무작위로 리스트에 집어넣음
for i in range(n):
    num = random.randint(1, 100)
    sample.append(num)

print("="*20)
print("입력리스트")
print(f"{sample}")
print("="*20)

# 반복할 숫자를 높이면 평균이 50에 비슷해짐
print(f"평균={statistics.mean(sample)}")
print(f"중간값={statistics.median(sample)}")
print(f"최빈값={statistics.mode(sample)}")
print(f"표준편차={statistics.stdev(sample)}")