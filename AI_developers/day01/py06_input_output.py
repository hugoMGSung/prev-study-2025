# py06_input_output.py
# 입출력

# 입력받는 함수. 입력에서 엔터가 들어올때까지 대기
name = input('당신의 이름을 입력하세요 > ')
print('안녕!', name)

age = int(input('당신의 나이를 입력하세요 > ')) # 나이를 입력하면 정수화
# print(type(age))
if age > 40:
    print('어휴, 나이많이 먹으셨네요.')
else:
    print('아직 젊군!')

## 다중입력 처리
word1, word2 = input('영단어 두개를 입력하세요 > ').split()
print('첫번째 단어', word1)
print('두번째 단어', word2)
