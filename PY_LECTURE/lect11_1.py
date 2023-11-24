# 파일 출력
"""
# 파일 생성
'''
from faker import Faker as fk
import os

# temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)

with open(folder + "fktemp.csv", "w", encoding='utf8') as f:
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "w", newline='', encoding='utf8') as f:
    for i in range(30):
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
'''

# 파일 열기
'''
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

# 순위 매기기
print("\n---------------------\n")

df["aver"] = df.postcode.rank(method = "average")
print(df["postcode", "aver"])

df["dense"] = df.postcode.rank(method = "dense")
print(df["postcode", "dense"])

df["first"] = df.postcode.rank(method = "first")
print(df["postcode", "first"])

df["min"] = df.postcode.rank(method = "min")
print(df["postcode", "min"])

# df["max"] = df.postcode.rank(method = "min", ascending = False)

df["max"] = df.postcode.rank(method = "max")
print(df["postcode", "max"])

# 전치 컬럼 = 로우변환
print("\n---------------------\n")
print(df.transpose())

# 누적 계산
print("\n---------------------\n")
print(df["postcode"].expanding().sum())
print(df["postcode"].expanding())

# 내림차순 기준
print("\n---------------------\n")
print(df.postcode.idxmax(axis = 0)) # 가장 작은수
print(df.postcode.idxmin(axis = 0)) # 가장 큰수

# empty 추가
print(df.empty)
print(df.postcode.empty)

# 인자 검색
print("\n---------------------\n")
print(df.isin([99326]))
print(df.isin(['문지아']))
print(df.isin([99326, 13016]))
print(df.isin([99326, 13016, '문지아']))

# 기간 계산
print("\n---------------------\n")
# period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data = dt, index = idx)
print(pf)

# 인덱스 시간 - 간격 생성
print("\n---------------------\n")
# i = pd.date_range("2023-11-10", periods=10, freq="1H")
i = pd.date_range("2023-11-10", periods=10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

# 특정시간 찾기
print("\n---------------------\n")
print(df.at_time("09:00"))
print(df.at_time("03:00"))

# 범위 찾기
print("\n---------------------\n")
# print(df.between_time(start_time="12:00", end_time="00:00"))
print(df.between_time(start_time="03:00", end_time="09:00"))

# X일 간격 생성 - 기간별 찾기
print("\n---------------------\n")
i = pd.date_range("2023-11-10", periods=10, freq="3D")
# i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print(df.first("5D"))

print(df.first("7D"))

print(df.last("7D"))
'''
"""

# 코스피지수
"""
import FinanceDataReader as fdr

ksp = fdr.DataReader("KS11", "2023")
print(ksp)
print("\n---------------------\n")

# 최고가
res = ksp["High"].max()
print(res)

res = ksp["High"].idxmax()
print(res)

# 최저가
res = ksp["Low"].min()
print(res)

res = ksp["Low"].idxmin()
print(res)

# 최고가 찾기
res = ksp["Volume"].nlargest(n=5)
res = ksp["Volume"].nlargest(n=10)
# res = ksp["Close"].nlargest(n=5)
print(res)

# 최저가 찾기
res = ksp["Volume"].nsmallest(n=5)
res = ksp["Close"].nsmallest(n=5)
print(res)

# kospi 3000 달성 최초일 찾기
cond = ksp["Close"] >= 3000
res = ksp[cond].index[0]
print(res)

# kospi 2000 달성 최초일 찾기
cond = ksp["Close"] >= 2000
res = ksp[cond].index[0]
print(res)

# 위 값 참조 처리
ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
print(ksp)

res = ksp["up"] != ksp["up"].shift().cumsum()
print(res)

ksp["grp"] = (ksp["up"] != ksp["up"].shift()).cumsum()
print(ksp)

# 연속 증가값 확인
ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(ksp)

# 연속 상승값 확인
print(ksp["up_cnt"].max())
"""

# 부동산 정보 처리
"""
# 변환
'''
import pandas as pd

target = "./data/apt.csv"

df = pd.read_csv(target, encoding = "CP949")

df.to_csv("./data/conv_apt.csv", encoding = "utf8")

print(df.head())
'''

import pandas as pd

df = pd.read_csv("./data/conv_apt.csv", index_col = 0)
print(df.head())

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
print(df)
print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
print(df.dtypes)

# array 변환
arr = df.to_numpy()
print(arr)
print(arr[2])
print(len(arr))

print(df.describe())

print(df.transpose())
print("\n---------------------\n")
print(df.T.head())
"""