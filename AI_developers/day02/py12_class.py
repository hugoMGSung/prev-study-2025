# py12_class.py
# 객체지향, 클래스

# 클래스 정의
class Person:
    name = ''  # 속성, 명사, 클래스 멤버변수
    age = 0
    weight = 0.0

    # 행위, 동사, 클래스 멤버함수
    # 1번 초기화 
    def __init__(self):
        self.name = '홍길동'
        self.age = 99
        self.weight = 60

    def __str__(self):
        return f'이름은 {self.name} / 나이는 {self.age} 살'
    
    def getup(self):
        return f'{self.name}이(가) 아침에 일어납니다.'
    
    def say_hello(self, yourname):
        print(f'{self.name}가 인사합니다. {yourname} 안녕!!')
        return None # 이부분은 생략    

# 클래스 사용 -> 객체 생성
hugo = Person()
# print('hugo -> ', hugo.name)
# print(hugo.age)
hugo.name = '유고'
hugo.age = 49
hugo.weight = 79.2
print(hugo)
print(hugo.getup())
hugo.say_hello('애슐리')

ashely = Person()
# print('ashely -> ', ashely.name)
# print(ashely.age)
ashely.name = '애슐리'
ashely.age = 40
ashely.weight = 0.1
print(ashely)
print(ashely.getup())

# hugo.name = '유고'
# hugo.age = 49
# hugo.weight = 79.2

# print(f'이름은 {hugo.name}')
# print(f'나이는 {hugo.age}')
# print(f'몸무게는 {hugo.weight}')