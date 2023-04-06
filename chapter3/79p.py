num = int(input("상품은 총 몇 개 인가요? : "))

sum = 0
for i in range(num):                        # num번 반복
    name = input("제품의 이름은 무엇인사요? : ")
    price = int(input("얼마 인가요? : "))
    amount = int(input("몇개가 팔렸나요? : "))

    print(name + "이라는 제품의 가격은", str(price) + "이고", str(amount) + "개 팔렸습니다.")
    sum += amount * price                   # 총매출 구하기

print("총 매출은", str(sum) + "입니다.")        # 총매출 출력