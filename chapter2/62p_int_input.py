print("두수의 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지를 구하는 프로그램입니다.")

a = int(input("첫번째 숫자 입력"))
b = int(input("두번째 숫자 입력"))

sum = a + b     #덧셈
sub = a - b     #뺄셈
mul = a * b     #곱셈
div = a / b     #나눗셈
quo = a // b    #몫
rem = a % b     #나머지

print(a, "과",b , "의 합은", sum, "입니다")
print(a, "과",b , "의 뺄셈은", sub, "입니다")
print(a, "과",b , "의 곱하기는", mul, "입니다")
print(a, "과",b , "의 나누기는", div, "입니다")
print(a, "과",b , "의 몫은", quo, "입니다")
print(a, "과",b , "의 나머지는", rem, "입니다")