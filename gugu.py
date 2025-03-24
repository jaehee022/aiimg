# 사용자로부터 입력을 받는 함수
dan = int(input("구구단의 단을 입력하세요: "))

# 입력받은 단에 대한 구구단 출력
print(f"==== {dan}단 ====")
for i in range(1, 10):  # 1부터 9까지 반복
    print(f"{dan} x {i} = {dan * i}")