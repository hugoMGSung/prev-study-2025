# AI개발자 과정 사전학습
- Python 기초

## 1일차

### 개발환경 설정

1. 압축프로그램 설치 - Bandizip
2. 코딩폰트 설치 - 나눔고딕, `D2Coding`
3. Visual Studio Code 설치
4. 마크다운 학습 - [링크](./markdown_basic.md)

### 파이썬 기초

#### 파이썬이란

네덜란드 개발자인 귀도 반 로섬(1956~)이 1990대경에 개발한 객체지향 프로그래밍 언어

#### 파이썬 설치

- https://www.python.org
- Windows 64bit Installer 설치할 것
- 마지막 Disabled path langth Limit 해제 클릭
- 설치 확인

```shell
> python --version
Pyhton 3.11.9
```

- VS Code 확장 > Python 검색 후 설치

#### 파이썬 실행
- VS Code, *.py 작성 후
    - 디버깅 없이 실행 Ctrl + F5

#### 파이썬 기본문법
- 프로그래밍언어 학습시 필요한 학습순서
    - 변수와 데이터 타입 
        - Integer, Float, Boolean, None, String, List, ...
    - 연산자
        - 사칙연산 + - * / // % ** 
        - 조건연산 > < >= <= == != ...
        - 문자열연산 + *
    - `흐름제어`
        - if - 참/거짓으로 분기
        - for - 반복처리
        - while - 반복(for문과 1:1 매핑)
    - 화면입출력, 문자열 포맷팅
        - input(), print()
        - \r, \n, \t, \b, ...
        - %d, %f, %s, ...
        - `f'{name}`입니다.' 추천포맷

## 2일차
### 파이썬 기초
#### 파이썬 기본문법
- 파이썬 학습순서
    - 파일입출력
        - f = open(파일경로, mode='r|w|a', encoding='cp949|utf-8')
        - f.write(), f.readline()...
        - f.close()!
        - csv 파일 로드시 import csv
    - 함수
        - 한번이상 사용할 로직은 함수화
        - 재사용성, 코드절약
        - 함수를 많이 사용하면 복잡해짐
    - 클래스
        - 객체지향의 기본 단위
        - 프로그램상의 모든 것을 객체화해서 현실세계 유사한 개발 목적
        - 명사(속성, 멤버변수)와 동사(행위, 멤버함수)의 집합
        - 클래스를 생성 -> 객체
        - 함수보다 더 복잡
    - 모듈, 패키지
        - 모듈 - 파이썬 파일 하나 *.py
        - 패키지 - 파이썬 파일이 모여있는 폴더(디렉토리)
        - pip, Pypi.org 
    - 예외처리 및 디버깅
        - 에러(Error) - 문법상 오류. 해결이 쉽다
        - 예외(Exception) - 실행상 발생하는 오류. 잡기가 무지 어려움. 반복훈련, 습관화
        - 디버깅 - F9, F5, F10, F11, Shift-F5
        - try ~ except ~ finally 로직 작성

## 3일차
### 파이썬 기초
#### 파이썬 응용
- 토이프로젝트 
    1. 주소록 콘솔앱
        1. 콘솔(터미널)에서 실행되는 주소록 관리 프로그램
        2. 연락처추가, 출력, 삭제 위주 - CRUD중 CRD만 개발
        3. 파일DB사용 데이터 관리
        4. 디버깅 및 예외처리
        5. 편의성(데이터수), 메시지 추가
        6. 파일구분
            - addressbook.py
            - address.py
            - address_db.txt

    2. chatGPT 따라만들기(GUI앱)
        1. 구글 제미나이 API 신청 - https://aistudio.google.com/apikey?hl=ko
        2. 테스트 - 주피터노트북
        3. tkinter GUI 개발
        4. 제미나이를 tkinter에 접목