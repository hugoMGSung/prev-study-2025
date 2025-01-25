# py09_csvfile_read.py
# csv파일 텍스트읽기

# encoding = cp949(ANSI, euc-kr) 인지 utf-8 인지 잘 파악
f = open('./day02/부산광역시 금정구_국민기초생활보장수급자 현황_20240430.csv', mode='r', encoding='utf-8')

while True:
    line = f.readline()
    if not line: break

    print(line)

f.close()