# 내장 함수
# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())
print("---")
print(dir(random))

# list of python builtins 검색
# https://docs.python.org/ko/3/library/functions.html 에서 내장 함수들 확인 가능

# 외장 함수
# list of python modules 검색
# https://docs.python.org/3/py-modindex.html

# glob: 경로 내의 폴더/파일 목록 조회
import glob
print(glob.glob("*.py"))

# os: 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재 하는 폴더")
    os.rmdir(folder )
    print(folder, "폴더를 삭제함.")
else:
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성함.")

print(os.listdir())

print("----------------")

# time
import time
print(time.localtime())
print(time.strftime("%Y-%M-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())
# timedelta: 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("오늘부터 100일 후 정보", today + td)

print("지금 시간은", datetime.datetime.now())