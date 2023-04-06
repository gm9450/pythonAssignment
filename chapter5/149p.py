# 컴퓨터 제어하기

# ---수정사항---
# 현재작업경로, 경로변경, 파일목록확인 하는 기능을 추가하였다.

import os
while True:
    print("-----------")
    print("1 : 현재 작업 경로\n2 : 작업 경로 변경\n3 : 현재 경로의 파일 목록\n4 : 종료")
    print("-----------")
    command = int(input("명령을 입력하시오 : "))
    if (command == 1):
        cwd = os.getcwd()
        print("현재 작업 경로 :", cwd)
    elif (command == 2):
        wd = input("이동할 경로를 적어주세요. : ")
        os.chdir(wd)
    elif (command == 3):
        path = os.getcwd()
        files = os.listdir(path)
        print(files)
    elif (command == 4):
        print("종료합니다.")
        break
    else :
        print("잘못된 명령입니다.")