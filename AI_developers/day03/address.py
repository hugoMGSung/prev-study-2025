# address.py
# 주소정보 클래스

# 2. 클래스 선언
class Address:
    def __init__(self, name, phone, email, street):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__street = street

    # 4. 사용자가 볼수 있도록 출력변경
    def __str__(self):
        str_ = (f'이  름: {self.__name}\n'
                f'모바일: {self.__phone}\n'
                f'이메일: {self.__email}\n'
                f'거주구: {self.__street}')
        return str_
    
    # 13. 주소록 클래스에 해당 주소가 있는지 판별
    def isNameExist(self, name) -> bool:
        if self.__name == name:
            return True
        else:
            return False
        
    # 15. 주소록 클래스에서 각 속성값 가져오는 멤버함수
    def getName(self):
        return self.__name
    
    def getPhone(self):
        return self.__phone
    
    def getEmail(self):
        return self.__email
    
    def getStreet(self):
        return self.__street
    
