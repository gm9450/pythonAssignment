import math

print("상용로그표를 출력합니다.")
print("1.00부터 1.99까지 출력합니다.")

for n in range(100):                # 100번 반복
    log_num = 1.0 + n/100           # 1.01부터 1.99까지
    log_10 = math.log(log_num, 10)  # 상용로그 저장
    log_10_s =  round(log_10, 4)    # 자릿수를 소수점부터 4자리까지로 제한

    print(log_10_s, end = ' | ')    # 출력
    if(n%10 == 0) :                 # 10으로 나눠지면
        print('\n')                 # 가독성을 위해서 줄바꿈해줌