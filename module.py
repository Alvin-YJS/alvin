"""
import random

# 1부터 10까지의 정수 중에서 랜덤으로 선택
print(random.randint(1, 10))

# 리스트에서 랜덤으로 하나 선택
my_list = ["apple", "banana", "cherry"]
print(random.choice(my_list))

# 0.0과 1.0 사이의 랜덤 실수 생성
print(random.random())

#정규 분포를 따르는 랜덤 실수 생성
print(random.normalvariate(0, 1))
"""


# 모듈화
"""
import mod.utils as mu

my_list = ["apple", "banana", "cherry"]
print(mu.rd_int(1, 100))
print(mu.rd_list(my_list))
print(mu.rd_rd())
print(mu.rd_normalvariate())
"""

# datatime 이용 함수

from datetime import datetime as dt

"""
# 현재 시간 출력
print(dt.now())

# 특정 시간대의 현재 시간 출력
#from pytz import timezone
import timezone
# tz = timezone("Asia/Seoul")
tz = timezone("UTC")
print("timezon : ", dt.now(tz))
"""

"""
# 문자열을 날짜로 변환
date_string = "2021-07-08"
date_object = dt.strptime(date_string, "%Y-%m-%d")
print(date_object)

# 날짜를 문자열로 변환
date_object = dt.now()
date_string = date_object.strftime("%Y-%m-%d")
print(date_string)

import mod.utils as mu
#import datetime as dt

#print(dt.now)
dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time
print(res)
"""

# os 모듈
"""
import os

# 현재 작업 디렉토리 출력
print(os.getcwd())

# 디렉토리 변경
os.chdir('../')

# 변경된 디렉토리 출력
print(os.getcwd())

# 파일 목록 출력
print(os.listdir())

# 디렉토리 삭제
os.rmdir('new_diresctory')
print(os.listdir())

# 디렉토리 생성
os.mkdir('new_direstory')
print(os.listdir())
"""

"""
import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir())
"""

"""
import sys
print(sys.version)
print(sys.argv)
"""

# stack
"""
st = []

# 스택에 값 넣기
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

# 스택의 상태 확인
print(st) # [1, 2, 3]

# 스택에서 값 빼기
top = st.pop()
print(top) # 3
print(st) #
print(len(st)) # 
"""

# append, pop을 이용한 queueS
"""
# 빈 큐 생성
queue = []

# 큐에 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# 큐의 상태 확인
print(queue) # [1, 2, 3]

# 큐에서 간 빼기
front = queue.pop(0)
print(front) # 1
print(queue) # [2, 3]
print(len(queue))
"""