# py04_flow_control.py
# 흐름제어

## if, for, while
### if
age = 16

if age >= 19:  # 조건이 참이면
    print('담배드릴게요')
    print('4,500원입니다.')
else:   # 조건이 거짓이면
    print('뒤질래? 집에가!')

### for (프로그래밍의 꽃!)
# print(range(5))
for number in range(1, 10 + 1):
    print(number)

# 아래와 같이 출력되는 프로그램을 작성하라
'''
*
**
***
****
*****
'''
for i in range(1, 6):
    print('*' * i)

sum = 0
for i in range(1, 10 + 1):
    sum = sum + i

print(sum)

## while - for와 동일. 서로간 변환 가능
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1

print(sum) 

i = 0
while True: # 무한반복(Infinite Loop)
    i = i + 1
    print('number:', i)