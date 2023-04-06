# 구구단 출력

# ---수정사항---
# 두정수를 입력받음
# 작은 정수부터 큰 정수까지의 구구단을 출력

def ggd(n):
    for i in range(1, 10, 1):
        print(f"{n} x {i} = {n*i}")

print("몇 단부터 몇단까지 출력할까요?")
n1 = int(input("정수를 입력해주새요. : "))
n2 = int(input("정수를 입력해주새요. : "))

if (n1 >= n2):
    while (n1 >= n2):
        print(n2, "단")
        ggd(n2)
        n2 += 1
elif (n1 < n2):
    while (n2 > n1):
        print(n1, "단")
        ggd(n1)
        n1 += 1
