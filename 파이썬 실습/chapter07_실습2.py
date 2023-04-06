# 시저 암호

# 평문 입력(영문 소문자, 대문자, 공백)
# 키(0~25) 입력
# 암호문 출력
# 키 값 만큼 평문 알파벳이 시프트 됨
# 공백은 암호화 되지 않음

pt = input("평문 = ")
key = int(input("키 = "))
ct = ""

for i in range(len(pt)):
    # 영문자 이외의 경우
    if (pt[i] == " "):
        ct += pt[i]
    else :
        # 소문자인 경우
        if (pt[i] >= 'a'):
            # key값 이동후 소문자가 아니게 된 경우
            if (ord(pt[i]) + key > ord('z')):
                ct += chr(ord(pt[i])+key-ord('z')+96)
            # 일반적으로 key값만큼 이동
            else:
                ct += chr(ord(pt[i])+key)
        # 대문자인 경우
        elif (pt[i] < 'a'):
            # key값 이동후 대문자가 아니게 된 경우
            if (ord(pt[i]) + key > ord('Z')):
                ct += chr(ord(pt[i])+key-ord('Z')+64)
            # 일반적으로 key값만큼 이동
            else:
                ct += chr(ord(pt[i])+key)
               
# 암호문 출력
print(ct)