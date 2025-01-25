# py08_file_inout.py
# 파일 입출력

# 파일오픈 open(경로및파일명, 오픈모드, 인코딩)
# mode=w(rite),r(ead), a(ppend)
# encoding=cp949(euc-kr), utf-8
f = open('./day02/test.txt', mode='w', encoding='utf-8') # 파일 쓰기
f.write('------------------------------------\n')
f.write('저는 개발자입니다.\n')
f.write('저는 한국사람입니다.\n')
name = '유고'
f.write(f'제이름은 {name}입니다.\n')

f.close()
print('파일이 생성되었습니다.')

r = open('./day02/test.txt', mode='r', encoding='utf-8') # 파일 읽기
while True:
    line = r.readline() # 한줄씩 읽어옴
    if not line: # 한줄 읽은게 None
        break # 반복문 탈출

    print(line.replace('\n', '')) # 읽어온 내용 화면에 출력

r.close()