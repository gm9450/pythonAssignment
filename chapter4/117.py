import random

# 문제, 답 정리
a = "파이썬은 인터프리터 언어인가 컴파일 언어인가?"
a_a = "인터프리터 언어"

b = "머신러닝 프로그래밍, 데이터 분석, 사물 인터넷, 수치 연산, GUI프로그램밍 등에 많이 쓰이는 언어는?"
b_a = "파이썬"

c = "\"123\"은 무슨 자료형인가?"
c_a = "문자열"

d = "for나 while은 어떤 동작을 수행하나요?"
d_a = "반복"

e = "몫을 구하는 연산자는?"
e_a = "//"

f = "아스키코드는 하나의 문서에 여러 나라의 언어를 동시에 표현할 방법이 없었는데 이를 해결한 문자는?"
f_a = "유니코드"

# 퀴즈들을 리스트에 저장함
question = [a, b, c, d, e, f]
answer = [a_a, b_a, c_a, d_a, e_a, f_a]

print(f_a)

# 퀴즈의 개수를 물어봄 1~6개
n = int(input("몇개의 퀴즈를 낼까요? : "))

# 퀴즈 문제와 정답 확인하기
for i in range(n):              # 개수 만큼 반복
    num = random.randint(0, 5)  # 랜덤으로 문제를 선택함
    text = str(question[num]) + " : "
    s = input(text)
    print(str(answer[num])==s)