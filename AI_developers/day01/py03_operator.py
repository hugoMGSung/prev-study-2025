# py03_operator.py
# 연산자 학습

## + - * / ()
a = 12
b = 4

# 사칙연산
print('==> 사칙연산')
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 3.0
b = 5
print(a / b)  # 2.4
print(type(a / b)) # 실수타입
print(a // b) # 나누기 몫
print(type(a // b)) # 정수타입
print(a % b)  # 나누기 나머지

print(2 ** 10)  # 2의 10승

# 문자열연산,  +(문자열합치기), *(문자열반복수)
print('==> 문자열연산')
greeting = 'Hello'
lang = 'Python'
print(greeting + lang)
print(greeting * 4)

# 비교연산
print('==> 비교연산')
print(a == b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)