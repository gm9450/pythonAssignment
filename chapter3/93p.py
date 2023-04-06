import random

print("랜덤으로 두수를 뽑아 더하기 문제를 내는 프로그램 입니다.")
print("총 10문제로 구성되어 있습니다.")
n = int(input("0부터 몇까지의 숫자를 뽑을가요? : "))
score = 0
for i in range(10):                          # 10번 반복
    a = random.randint(0, n)                 # 랜덤 숫자 뽑기
    b = random.randint(0, n)
    num = a + b
    print(a, "+", b, "을 구하시오.")
    ans = int(input("정답을 입력해주세요. : "))  # 정답 입력
    if (ans == num):                         # 정답이라면
        score += 1
        print(i+1, "번쩨 정답")
    else:                                    # 틀렸다면
        print(i+1, "번째 틀림")

print("="*30)
print("10문제 중", str(score) + "개 맞았습니다") # 맞은 갯수 공개
print("="*30)