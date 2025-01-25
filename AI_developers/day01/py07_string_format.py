# py07_string_format.py
# 문자열 포맷팅

numbers = [1,2,3,4,5]
print(numbers[4]) # indexing

words = 'Hello'
print(words[0])

## 문자열 연산
current = '2025-01-21 16:09:51'
print(current)

year = current[:4]
print(year)
month = current[5:7]
print(month)
day = current[8:10]
print(day)
hour = current[11:13]
print(hour)
second = current[17:]
print(second)
second2 = current[-2:] # 오른쪽 끝에서부터 거꾸로 셀 수있음
print(second2)

temp = current.split() # 공백으로 잘라 배열로 만들어주는 함수
cdate = temp[0]
ctime = temp[1]

cyear, cmonth, cday = cdate.split('-')
chour, cminute, csecond = ctime.split(':')

print(cday, cmonth, cyear, csecond, cminute, chour)

인사 = 'Hello, Python'
print(인사.replace('o', ''))

## 문자열 포맷팅
### Escape 문자 \r \n \t \b \' \" \\ \f
print('Sayonara\n\t\bIchiban!')

print('\'test\'')
print("'test'")
print('"Hello"')

### %d(정수), %f(실수), %s(문자열)
# 초구닥다리 방식
print('저는 %s이고, %03d대 개발자입니다. 몸무게는 %.1fkg입니다' %('유고', 40, 76.5))

# 구닥다리 방식
print('저는 {0}이고, {1:03}대 개발자입니다. 몸무게는 {2}kg입니다'.format('유고', 40, 76.5))

# 최신방식
name = '유고'
age = 40
weight = 76.5
print(f'저는 {name}이고, {age:03}대 개발자입니다. 몸무게는 {weight:.2f}kg입니다')