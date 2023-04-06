friend_list = []
friend_data = []

n = int(input("친구 몇명을 입력할까요? : "))
print("\n")

for i in range(n):
    friend = input("이름을 입력해주세요. : ")
    friend_list.append(friend)

    n1 = input("친구의 특징이 있나요?(y, n으로 대답) :")      # 특징 개수
    
    if (n1 == 'y'):
        friend_d = input("특징을 입력해주세요. : ")
        friend_data.append(friend_d)                    # "특징 추가"
    else:
        friend_data.append("특징 없음")                   # "특징 없음"을 친구 정보 리스트에 추가함

    print("\n")

print("="*20)
for i in range(n):
    print(friend_list[i], "의 특징은")
    print(friend_data[i], "입니다.")
print("="*20)

print("친구는 총", n, "명 있습니다.")
print(friend_list)
print(friend_data)