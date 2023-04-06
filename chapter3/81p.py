money = int(input("투입한 돈 : "))
price = int(input("물건값 : "))

change = money-price
print("거스름돈 : ", change)

# 거스름돈 분류하기
coin500s = change // 500
change = change % 500
coin100s = change // 100
change = change % 100
coin50s = change // 50
change = change % 50
coin10s = change // 10

print("500원의 개수 :", coin500s)
print("100원의 개수, :", coin100s)
print("50원의 개수 :", coin50s)
print("10원의 개수 :", coin10s)

# 자판기에서 동전이 반환될떄 나오는 메시지
print("="*30)
for i in range(coin500s) :
    print("500원이 반환되었습니다.")
    print("남은 500원의 개수 :", coin500s - (i + 1))

print("="*30)
for i in range(coin100s) :
    print("100원이 반환되었습니다.")
    print("남은 100원의 개수 :", coin100s - (i + 1))

print("="*30)
for i in range(coin50s) :
    print("50원이 반환되었습니다.")
    print("남은 50원의 개수 :", coin50s - (i + 1))

print("="*30)
for i in range(coin10s) :
    print("10원이 반환되었습니다.")
    print("남은 10원의 개수 :", coin10s - (i + 1))

print("="*30)
print("동전이 모두 반환 되었습니다.")