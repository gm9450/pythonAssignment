# 1부터 n까지의 합 계산

# ---수정사항---
# 재귀함수로 표현함

def sum(n):
    if (n == 1):
        return 1
    return n + sum(n-1)

print("1부터 n까지의 합을 구합니다.")
n = int(input("정수를 입력하시오. : "))
print("합계는", sum(n))