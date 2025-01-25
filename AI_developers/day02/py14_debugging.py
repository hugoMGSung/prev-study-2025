# py14_debugging.py
# 디버깅, 예외처리
# Error 분류
#  1. 문법오류 -> 에러(Error)!!
#  2. 실행오류 -> 예외(Exception)

# 디버깅
#  F9 - 브레이크포인트 토글
#  F5 - 디버그 실행 또는 BP까지 실행
#  F10 - 한줄 실행
#  F11 - 내부로직 진입
#  Shift + F5 - 디버깅 종료

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def divide(a, b):
    # 예외가 발생할 수 있는 로직에 예외처리 코드 추가
    # try - except - [finally]
    try:
        result = str(a / b)
    except:
        print('예외발생 : 0으로 나누지 말것')
        result = 'INF'
    
    return result

x, y = 14, 3
print(f'더하기, {x} + {y} = {add(x, y)}')
x, y = 17, 0
print(f'나누기, {x} ÷ {y} = {divide(x, y)}')
x, y = 24, 7
print(f'빼기, {x} - {y} = {minus(x, y)}')
print('계산종료!')