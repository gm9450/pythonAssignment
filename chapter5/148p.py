# 로그인 프로그램

# ---수정사항---
# 비번 입력을 추가함 

id = "i lovepython"
pw = "pythonlove2023"
s = input("아이디를 입력하시오 : ")
p = input("비번을 입력하시오 : ")

if (s == id and p == pw):
    print("환영합니다.")
else :
    print("아이디나 비번이 다릅니다.")