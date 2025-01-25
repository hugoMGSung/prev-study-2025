# py16_tkinter_app.py
# GUI 개발시작
import tkinter as tk
from tkinter import scrolledtext, messagebox
# 3. 제미나이 API용 모듈
import google.generativeai as genai

# 1. 메인윈도우 생성
root = tk.Tk() 
root.title('Tkinter App')   # 윈도우 창제목 설정
root.geometry('730x465')    # 윈도우 창크기(Geometry)
root.iconbitmap('./day03/chatbot.ico')

# 4. 제미나이AI용 API 구성
genai.configure(api_key='AIzaSyB0HR41I19x8f-qMJUkMS0PBpoDlINWsOk')
model = genai.GenerativeModel('gemini-1.5-flash') # 사용할 AI모델 지정

prompt = ('저는 구글 젬봇입니다. 질문에 답하고 여러 작업을 돕기위해 설계된 여러분의 조수입니다.\n'
          '필요한 것이 있으면 그냥 물어보세요!')

# 5. 응답을 생성하는 함수
def generate_response():
    # .replace('\n', '') - 쓸모없는 엔터를 제거
    # .strip() - 입력시 생기는 불필요한 스페이스 제거
    input_text = user_input.get('1.0', tk.END).replace('\n', '').strip() # 사용자가 입력하는 텍스트
    # print(input_text)
    if input_text: # 입력한 글이 있으면
        try:
            # 입력메시지를 채팅패널에 표시
            chat_pannel.insert(tk.END, '메시지: ', 'bold') # '메시지: '글자를 굵게 표시
            chat_pannel.insert(tk.END, f'{input_text}\n', 'user')

            # 사용자 입력과 챗봇의 소개메시지를 결합
            total_prompt = f'{prompt}\n\n메시지: {input_text}\n젬봇: '

            # 제미나이 AI 전송
            ai_response = model.generate_content(total_prompt)
            response = ai_response.text # 생성된 응답 중 텍스트만 추출

            # 9. 응답에 원하지않는 AI관련 내용이 포함될때, prompt가 뜨도록
            if 'large language model' in response or \
               'Google AI' in response:
                response = prompt   # 소개글이 나오도록               

            # AI 응답을 채팅패널에 표시
            chat_pannel.insert(tk.END, '젬봇: ', 'bold')
            chat_pannel.insert(tk.END, f'{response}\n', 'ai')            
        except Exception as e:
            # 예외발생시 채팅패널 출력
            chat_pannel.insert(tk.END, f'Error: {str(e)}\n', 'error')
        finally: # 예외발생 하든 안하든 입력박스 삭제와 채팅패널 스크롤 다운은 무조건 실행
            # 입력박스 삭제
            user_input.delete('1.0', tk.END)
            # 채팅패널 스크롤다운
            chat_pannel.see(tk.END)

# 7. keypress 이벤트처리함수
def keypress(event): 
    # print(repr(event.char)) # 키보드 입력값 확인
    if event.char == '\r':
        generate_response()

def on_closing():
    # '종료하시겠습니까?' 확인창
    if messagebox.askokcancel('종료 확인', '종료하시겠습니까?'):
        root.destroy() # 정말 종료!

# 2. UI 구성
# 채팅패널(스크롤 가능)
chat_pannel = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=('NanumGothic', 10), bg='#000000', fg='white')
chat_pannel.pack(padx=10, pady=10, fill=tk.BOTH, expand=True) # 채팅패널을 윈도우 배치

# 6. 사용자와 제미나AI 메시지 간의 태그 및 디자인 설정
chat_pannel.tag_configure('user', font=('NanumGothic', 10, 'bold'), foreground='yellow') # 사용자 메시지
chat_pannel.tag_configure('ai', font=('NanumGothic', 10), foreground='limegreen') # #89F336
chat_pannel.tag_configure('bold', font=('NanumGothic', 10, 'bold')) 
chat_pannel.tag_configure('error', font=('NanumGothic', 10, 'italic'), foreground='red')

# Red(1byte: 0~255) Green(1byte) Blue(1byte)
# 255까지의 10진수를 16진수로 표현 00(0) ~ FF(255)
# #000000 -> black, #FFFFFF -> white
input_frame = tk.Frame(root, bg='#EFEFEF')
input_frame.pack(fill=tk.X, padx=10, pady=5) # 입력 프레임을 윈도우 배치

# 사용자 input
user_input = tk.Text(input_frame, height=1, font=('NanumGothic', 10), wrap=tk.WORD)
# 7. 사용자 키보드입력 처리
user_input.bind('<Key>', keypress) # 키보드 입력이 확인되면 keypress 함수를 실행하라!
user_input.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True) # 입력박스를 input_frame의 왼쪽 배치

# 실행버튼
proc_button = tk.Button(input_frame, text='실행', font=('NanumGothic', 10), bg='blue', fg='white',
                        command=generate_response) # 실행버튼 클릭 generate_response() 함수 실행
proc_button.pack(side=tk.RIGHT, padx=5, pady=5) # 실행버튼을 input_frame 오른쪽 배치

# 10. chatGPT에게 물어본 종료버튼 확인메시지 처리
root.protocol('WM_DELETE_WINDOW', on_closing)

# 8. 프로그램 최초 실행시 user_input에 바로 입력가능하게 처리
user_input.focus_set() 

# 1. 실행(무한루프)
root.mainloop()