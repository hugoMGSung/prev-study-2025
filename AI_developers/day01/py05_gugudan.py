# py05_gugudan.py
# 구구단

for i in range(2, 10):
    # if i > 3: break   # 반복문 탈출
    print(i, '단 시작!')    
    for j in range(1, 10):
        # if j == 9: continue  # 그 부분만 스킵      
        print(i, 'x', j, '=', i * j, end='\t')
    print()
