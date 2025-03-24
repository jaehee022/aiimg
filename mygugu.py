# 숫자 두개를 입력을 받아서
# +, -, *, / 를 출력 하는 프로그램을 만들어 보자
a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b if b != 0 else '0으로 나눌 수 없습니다.'}")