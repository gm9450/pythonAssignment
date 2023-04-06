print("안녕하세요?")
name = input("이름이 어떻게 되시나요?")
print("\n만나서 반갑습니다.", name + "씨")
print("이름의 길이는 " + str(len(name)), "자리네요.\n")

# 첫번째 이름을 입력받으면  두번째 이름도 따로 프린트 할수 있음
first_name = input("성이 어떻게 되시나요?")
print("성은 " + first_name, "이고 이름은",
      name[(len(first_name))  : (len(name))],"네요." ,'\n')

# 나이를 입력받아서 태어난 년도를 출력함
age = int(input("나이가 어떻게 되시나요"))
print("내년이면 " + str(age+1) + "살이 되시는군요")
print(str(2023 - (age-1)) + "년에 태어나셨군요\n")

# 취미의 개수, 취미를 저장하여 모두 프린트 할 수 있음
n = 0
hs = ""
n = int(input("취미가 있나요? 있다면 몇개 있나요"))
for i in range(n):
    h = input("취미가 어떤 것인가요?")
    print(h + "라는 취미가 있으시군요\n")
    hs += h + ", "
print("취미로 ", hs[:len(hs)-2] + "들을 가지고 있군요")
