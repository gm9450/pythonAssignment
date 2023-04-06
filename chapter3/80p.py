temp = float(input("온도를 적어주세요. : "))                # float 타입으로 입력
unit = input(("단위를 적어주세요.(화씨 : f, 섭씨 : c) : "))   # 단위 입력

if (unit == 'f') :                                      # 화씨일때
    temp = (temp - 32)*5/9
    print("섭씨", str(temp) + "도 입니다.")
elif (unit == 'c') :                                    # 섭씨일때
    temp = temp*9/5 + 32
    print("섭씨",str(temp) + "도 입니다.")
else :
    print("잘못된 단위입니다")