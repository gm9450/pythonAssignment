# 윤년 판단 프로그램

# -- 수정사항---
# 무한루프를 사용함
# 기간동안의 윤년을 표시함
# 무한루프를 1,2,3 명령어를 통해 조작함
# 3을 입력시 무한루프를 탈출함

def leap_year(y) :
    if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        return True
    else :
        return False

while True:
    print("----------------")
    print("1 : 윤년 확인하기\n2 : 윤년표 확인하기\n3 : 종료")
    print("----------------")
    command = int(input("명령어를 입력해주세요. : "))
    if (command == 1) :
        year = int(input("연도를 입력해주세요. : "))
        if leap_year(year) :
            print("----------------")
            print(year, "는 윤년입니다.")
            print("----------------\n")
        else :
            print("----------------")
            print(year, "는 윤년이 아닙니다.")
            print("----------------\n")
    elif (command == 2) :
        year1 = int(input("어떤 년도 부터 확인할까요? : "))
        year2 = int(input("어떤 년도 까지 확인할까요? : "))
        print("----------------")
        if (year1 > year2):
            print("처음년도가 더 큽니다.")
            continue
        print("윤년은 ")
        while(year1 <= year2):
            if leap_year(year1):
                print(year1, "년")
            year1 += 1
        print("가 있습니다.")
        print("----------------\n")
    elif (command == 3):
        break
    else :
        print("제대로 입력해주세요.")