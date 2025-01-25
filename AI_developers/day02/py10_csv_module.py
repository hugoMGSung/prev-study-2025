# py10_csv_module.py
# csv파일 읽어오기2
import csv

f = open('./day02/부산광역시 금정구_국민기초생활보장수급자 현황_20240430.csv', mode='r', encoding='utf-8')

reader = csv.reader(f, delimiter=',') # 구분자가 , 일경우
next(reader)

for line in reader:
    print(line)

f.close()