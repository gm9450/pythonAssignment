# 사용자 입력하는 숫자 계산

# ---수정사항---
# 더하기, 빼기, 곱하기, 나누기를 이용해서 식을 생성 할 수 있음
# 식을 만듬
# 식에서 곱과 나눗셈에 우선순위를 부과함
# 양수-음수 식을 구현하지 못함

def form(formula):
    while True:
        number = float(input("양의 정수를 입력해주세요. : "))
        if (number <= 0):
            continue
        number = str(number)
        while True:
            unit = input("수식을 골라주세요(+,-,*,/, =) : ")
            if ((unit == "+") or (unit == "-") or (unit == "*") or (unit == "/") or (unit == "=")):
                return formula + number + unit
            else :
                print("잘못된 수식 입니다.")


# 곱과 나누기를 하는 함수
def calculate1(formula):
    integer1 = ""
    integer2 = ""
    for i in range(len(formula)):
        # 곱셈 나눗셈 먼저 계산
        if (formula[i] == "/" or formula[i] == "*"):
            integer1 = calculate_1(i - 1, formula)
            integer2 = calculate_2(i + 1, formula)
            if (formula[i] == "/"):
                integer = integer1 / integer2
                strinteger = str(integer)
                formula = form_new(i-1, i+1, formula, strinteger)
                return calculate1(formula)
            elif (formula[i] == "*"):
                integer = integer1 * integer2
                strinteger = str(integer)
                formula = form_new(i-1, i+1, formula, strinteger)
                return calculate1(formula)
    return calculate2(formula)

# 더하기 빼기를 하는 함수
def calculate2(formula):
    integer1 = ""
    integer2 = ""
    for i in range(len(formula)):
        if (formula[i] == "+" or formula[i] == "-"):
            integer1 = calculate_1(i - 1, formula)
            integer2 = calculate_2(i + 1, formula)
            if (formula[i] == "+"):
                integer = integer1 + integer2
                strinteger = str(integer)
                formula = form_new(i-1, i+1, formula, strinteger)
                return calculate2(formula)
            elif (formula[i] == "-"):
                integer = integer1 - integer2
                strinteger = str(integer)
                formula = form_new(i-1, i+1, formula, strinteger)
                return calculate2(formula)
    return calculate3(formula)
                    
# '='을 처리하는 함수
def calculate3(formula):
    integer = ""
    for i in range(len(formula)):
        if (formula[i] == "="):
            integer = calculate_1(i - 1, formula)
            return integer

# 수식 앞부분 숫자 추출 함수
# k는 수식이 있는곳보다 -1해서 계산, k의 위치는 숫자
def calculate_1(k, formula):
    integer = ""
    for i1 in range(k, -1, -1):
        unit = formula[i1 - 1]
        if ((unit == "+") or (unit == "-") or (unit == "*") or (unit == "/")):
            for i2 in range(i1, k+1):
                integer += formula[i2]
            return float(integer)
        elif(i1 == 0):
            for i2 in range(0, k+1):
                integer += formula[i2]
            return float(integer)

# 수식 뒷부분 숫자 추출 함수
# k는 수식이 있는 곳보다 +1해서 계산, k의 위치 숫자
def calculate_2(k, formula):
    integer = ""
    for i1 in range(k, len(formula)):
        unit = formula[i1]
        if ((unit == "+") or (unit == "-") or (unit == "*") or (unit == "/") or (unit == "=")):
            for i2 in range(k, i1):
                integer += formula[i2]
            return float(integer)

# 쓰여진 식은 지우고 새로운 식으로 만듬
def form_new(k1, k2, formula, integer):
    formula_new = ""

    for i1 in range(k1, -1, -1):
        unit = formula[i1 - 1]
        # i1이 0이라면 새로운 값을 집어 넣고 시작해야함
        if(i1 == 0):
            formula_new += integer
            break
        elif ((unit == "+") or (unit == "-") or (unit == "*") or (unit == "/")):
            for ik in range(0, i1):
                formula_new += formula[ik]
            formula_new += integer
            break
    for i1 in range(k2, len(formula)):
        unit = formula[i1]
        if ((unit == "+") or (unit == "-") or (unit == "*") or (unit == "/") or (unit == "=")):
            for ik in range(i1, len(formula)):
                formula_new += formula[ik]
            return formula_new

# 시작 함수
formula = ""
unit = ""
answer = ""
while (answer != "="):
    formula = form(formula)
    print("현재 식", formula)
    if (formula[len(formula)-1] == "="):
        break

print("-"*20)
print("최종 식")
print(formula)
print("정답 :", calculate1(formula))
print("-"*20)