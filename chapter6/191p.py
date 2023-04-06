# 암호 해독 프로그램

# ---수정사항---
# 컴퓨터가 (3개의 소문자 + 1개의 숫자)로 랜덤으로 비밀번호를 정함

import random
import sys

def password_fider(guess, password, user_pass):
    for letter1 in password:
        for letter2 in password:
            for letter3 in password:
                for integer in range(1, 10):
                    guess = letter1 + letter2 + letter3 +str(integer)
                    print(guess)
                    if (guess == user_pass):
                        return guess
        
guess = ""
user_pass = ""
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_pass += random.choice(password)
user_pass += random.choice(password)
user_pass += random.choice(password)
user_pass += str(random.randint(1, 9))

guess = password_fider(guess, password, user_pass)
print("컴퓨터가 찾은 패스워드 :", guess)
sys.exit()