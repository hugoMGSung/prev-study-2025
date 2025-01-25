# py02_variable.py
# 변수학습
# 2025-01-21 12:17
# Hugo MG Sung

box = 'apple'   # 문자열 String
print(box)

box = "파인애플" # 문자열 String
print(box)

box = False  # 거짓(참 True의 반대) True/False  Boolean
print(box)

box = 100_000_000  # 정수 Integer
print(box)

box = 3.14159262757  # 실수 Float
print(box)

box = [1,3,5,7,9]   # 배열 List
print(box)

box = ['apple', True, -10, 234.5, [1,2,3]]  # 복합배열
print(box)

box = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(box)

box = None # 아무것도 아님을 지칭하는 값
print(box)

box = ''  # Empty
print(box)


# 변수명은 사용법이 지정
samsung = 25
samsung2 = 000
samsung_3 = 111
_samsung = 222
박스 = '망고' # 한글사용가능
# 4samsung # 수로 변수명을 시작할 수 없음
# samsung! # ! 사용불가
# samsung-apple # - 사용불가
# if = 34 # 예약어는 사용불가

print(samsung == samsung2) # 둘의 값이 같은지 비교

print(samsung is samsung)