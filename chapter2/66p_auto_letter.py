print("친구에게 편지를 적어주는 프로그램입니다.\n")

# 구할 것
# 친구와 알고 지낸 시간을 year와 hour로 구하기

current_year = 2023
my_name = input("자신의 이름을 적어주세요 : ")
name = input("친구의 이름을 적어주세요 : ")
friend_age = int(input("친구의 나이를 적어주세요 : "))
meet_age = int(input("친구와 처음 알게된 나이를 적어주세요 : "))
name2 = input("또다른 친구의 이름을 적어주세요 : ")

print("="*40)
print("안녕", name, "잘지내니?")
print("우리가 처음", str(meet_age) + "살에 만나서", str(friend_age - meet_age), "이라는 시간이 지났구나")
print(name2 + "도 너에게 안부 전해달래")
print("우리", my_name, name, name2 + "이렇게 모여서 언제한번 밥먹자!\n")
print(name + "의 친구", my_name + "가")
print("="*40)
