# range() 함수 실습

# ---수정사항---
# n의 배수를 출력하는 프로그램으로 변경

print("100이하의 n의 배수를 출력하는 프로그램입니다.")
n = int(input("몇의 배수를 출력 할까요?"))

print(f"{n}의 배수")
for i in range(n, 101, n):
    print(f"변수 i의 값 = {i}")