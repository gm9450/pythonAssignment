a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

d = b**2 - 4*a*c
print("판별식이", d, "이다")               # 판별식 출력

if ( a != 0 ):
    if (d > 0):                         # 실근이 2개
        print("2개의 실근이 있다.")
        x1 = (((-b) + r**0.5)/(2*a))
        x2 = (((-b) - r**0.5)/(2*a))
        print("x =", x1, "or", x2)

    elif (d == 0.0):                    # 실근이 1개
        print("1개의 중근이 있다.")
        x = (-b)/(2*a)
        print("x =", x)

    elif (d < 0):                       # 실근이 없음
        print("실근이 없다.")

else :
    print("2차 방정식이 아닙니다.")