n = int(input("평균을 구할값의 갯수는 몇개입니까? : ")) # 반복할 정도 입력

sum = 0
for i in range(n):                              # n번 반복
    sum += int(input("값을 입력해주세요 : "))

avg = sum/n                                     # 평균 출력
print("평균 =", avg)