# 팩토리얼 계산하기

# ---수정사항---
# 팩토리얼을 재귀함수로 풀이 해봄
# 입력한 정수가 양수가 아닐시 오류 메시지를 전송함

def fec(n, formula):
    if (n < 0):
        return 0
    if (n == 0 or n == 1) :
        formula += "1"
        print(formula)
        return 1
    formula += str(n) + " x "
    return n * fec(n-1, formula)

print("팩터리얼을 계산합니다.")
n = int(input("정수를 입력하시오. : "))
f = fec(n, "")
if (f == 0):
    print("양수가 아닌 정수를 입력했습니다.")
else:
    print(f)
