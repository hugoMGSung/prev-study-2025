# py11_function.py
# 함수

# 함수정의
def say_hi():
    print('안녕~ ')
    return None
    
def say_hello(name):
    print(f'{name}야, 안녕!!')
    return None # 이부분은 생략

def real_age(age):
    return age - 1

def closing():
    return '바이바이'


# print('인사하기!')
# say_hi()    # 함수사용

# name = input('이름입력 > ')
# say_hello(name)

# age = int(input('나이입력 > '))
# rage = real_age(age)
# print(f'만나이는 {rage}')

# print(closing()) # == print('바이바이')