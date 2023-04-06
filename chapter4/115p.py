print("대문자만 출력하는 프로그램입니다.")
name = input("영어로 물체의 이름을 적어주세요")

# x를 리스트로 선언
x = []
for i in range(len(name)):  # 이름의 길이 만큼 반복
    if (name[i] < 'a'):     # 이름의 대문자를 가려내기 위한 조건
        x.append(name[i])   # 대문자를 리스트에 추가함

# p에 출력할 대문자를 저장함
p = ""
for i in range(len(x)): # 대문자의 개수 만큼 반복
    p += x[i]           # 대문자를 문자로 이어붙임

print("이 영어의 대문자는", p + "입니다.")