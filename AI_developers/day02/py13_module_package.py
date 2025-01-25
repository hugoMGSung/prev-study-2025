# py13_module_package.py
# 모듈과 패키지

# import py12_class as p
# import py11_function as F

# jin = p.Person()
# jin.name = '진'

# F.say_hi()

# import math 
from math import pi, sqrt, pow, cos, log2
import random

# print(math.cos(0))
# print(2 ** 10)
# print(math.pow(2, 10))
# print(math.log2(4))
pi * 10 * 10
sqrt(10)

# 엉망로또 645 
numbers = [i for i in range(1, 46)]
result = []
'''
여러줄 문자열을 여러줄 주석으로 대체 사용
두번째 줄
'''

for i in range(6):
    result.append(random.choice(numbers))

print(result)

## 기본패키지 사용중 urllib 웹사이트 오픈
## urllib 패키지 내 request.py 모듈 중 Request클래스와 urlopen 함수를 사용할 예정
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')
res = urlopen(req) # 웹사이트 오픈
print(res.status)

## requests 3rd party module
## pip - Package Installer for Python
## https://www.pypi.org - Python Package Index 웹사이트
## pip install requests
import requests

res2 = requests.get('https://www.naver.com')
print(res2.status_code)
print(res2.content)