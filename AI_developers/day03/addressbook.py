# addressbook.py
# 주소록 콘솔앱 - 메인

# 3. 모듈 추가
from address import Address # Address 만 사용하면 됨
import os  # 9. 화면 클리어용 모듈 추가

# 9. 화면클리어 - 프로그램 기능과는 무관
def clear_console():
    cmd = 'clear' # MacOS, Linux, Unix 화면클리어 명령어
    if os.name in ('nt', 'dos'): # OS가 Window라면
        cmd = 'cls' # Windows 화면클리어 명령어

    os.system(cmd)

# 5. 프로그램 실행 함수 - 실행에 필요한 기본함수
def run():
    # 11. 주소록 담는 변수
    lst_address = []  
    # 19. 주소록 읽어옴. address_db.txt에서 데이터 읽어오기 초기화
    load_address(lst_address)  
    # 10. 화면클리어 추가
    clear_console()

    # set_address()
    # 7. 메뉴에 따른 동작 구성
    while True:
        sel_menu = get_menu()
        if sel_menu == 1: # 11. 연락처 추가
            info = set_address()             
            if info is None: # None을 비교할때는 == 사용안함
                pass
            else:
                lst_address.append(info)

            input() # 화면전환 전 대기

        elif sel_menu == 2: # 12. 연락처 출력
            get_address(lst_address)
            input()

        elif sel_menu == 3: # 연락처 삭제
            name = input('삭제할 이름 입력 : ')
            del_address(lst_address, name)
            input()

        elif sel_menu == 4: # 종료
            # 17. 파일DB 저장
            save_address(lst_address)
            break 

        clear_console() # 10. 화면클리어 추가
    

# 8. 주소정보 받아서 객체 생성함수
def set_address():
    # 22. 주소입력을 잘못하면 아무것도 만들지 않음
    try:
        nm, pn, em, st = input('정보입력(이름,폰번호,이메일,주소 순)').split(',')
        # print(name, phone, email, street)
        addr = Address(name=nm, phone=pn, email=em, street=st)      
        return addr
    except:
        return None

# 12. 주소록 출력
def get_address(lst_address: list):
    print('==================')
    for addr in lst_address:        
        print(addr)
        print('----------')

    print(f'총 데이터수 : {len(lst_address)}')

# 14. 주소록 삭제
def del_address(lst_address: list, name: str):
    # enumerate() 열거시킨다. 배열 인덱스번호를 추가로 생성
    for i, addr in enumerate(lst_address):
        if addr.isNameExist(name): # 삭제할 이름이 존재한다면
            del lst_address[i] # 리스트 i번째 값을 메모리에 없애라!

# 16. 주소록 파일DB 저장
def save_address(lst_address):
    f = open('./day03/address_db.txt', mode='w', encoding='utf-8')
    # 쓰기
    for addr in lst_address:
        # 유고/7732/naver.com/남구
        f.write(addr.getName() + '/')
        f.write(addr.getPhone() + '/')
        f.write(addr.getEmail() + '/')
        f.write(addr.getStreet() + '\n')

    f.close()

# 18. 주소록 파일DB 읽어오기
def load_address(lst_address):
    f = open('./day03/address_db.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline()
        if not line: break  # 읽은 줄에 글이 없으면 == 마지막 줄이면(None)

        # line == 유고/7732/naver.com/수영구 
        # ==> 
        # lines == ['유고', '7732', 'naver.com', '수영구']
        lines = line.replace('\n', '').split('/') 
        # 20. 파일로드시 예외처리
        try: 
            addr = Address(name=lines[0], phone=lines[1], email=lines[2], street=lines[3])
            lst_address.append(addr)
        except IndexError as e:
            print('예외발생')

    f.close()

# 6. 메뉴구성
def get_menu():
    str_menu = ('주소록 프로그램 v0.2\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 프로그램 종료\n')
    print(str_menu)
    # 21. 메뉴선택시 수 이외에 값을 입력하면 생기는 예외 처리
    try:
        menu_num = int(input('메뉴입력 : '))
    except ValueError as e:
        print('예외발생')
        menu_num = 0 # 아무메뉴도 선택되지 않는 숫자로 지정

    return menu_num

# 1. 프로그램 시작
if __name__ == '__main__':
    # print('프로그램 시작')
    # print(__name__)
    # 3. 클래스를 실행
    # temp = Address('유고 성', '010-6688-7732', 'personar95@naver.com', '남구')
    # print(temp)
    run() 