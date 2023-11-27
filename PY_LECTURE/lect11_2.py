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
'''
arr = df.to_numpy()
print(arr)
print(arr[2])
print(len(arr))
'''

# 요약정보
'''
print(df.describe())
'''

# 축변환
'''
print(df.transpose())
print("\n---------------------\n")
print(df.T.head())
'''

# 정렬
'''
# res = df.sort_values (by = "지역명")[:5]
# print(res)

# res = df.sort_values (by = "지역명")
# res = df.sort_values ("지역명")
res = df.sort_values ("지역명", ascending = False)
# print(res.head(10))
# print(res.head())

# res = df.sort_values(by = "연도")
# res = df.sort_values(by = "부냥가")
# res = df.sort_values(by = "연도")[:5]
res = df.sort_values(by = "연도")[10:20]
print(res)
# print(res.head())
'''

# 컬럼이름 출력
'''
# res = df[["지역명"]][:5]
# res = df[["지역명", "연도"]]
# res = df[["지역명", "연도", "분양가"]]
res = df[["지역명", "연도", "분양가"]][:7]
# res = df[["지역명", "연도"]][:5]
print(res)

print("\n---------------------\n")
# res = df.loc[:, ["지역명", "연도"]][:5]
# res = df.loc[:, ["지역명", "연도", "분양가"]][:5]
# res = df.loc[:][:5]
# res = df.loc[:][:]
res = df.iloc[1]
print(res)

# res = df.loc[:6, ["지역명", "연도"]]
# res = df.loc[:6, ["지역명", "연도"]][:3]
res = df.loc[:6, ["지역명", "연도"]][3:]
# res = df.loc[:6, ["지역명", "연도"]][:7]
print(res)
'''

# 필터 출력
'''
# res = df.loc[df["지역명"] == "강원"]
# res = df.loc[df["연도"] > 2020]
# res = df.loc[df["지역명"] == "서울",["지역명", "연도", "분양가"]]
# res = df.loc[df["지역명"] == "서울",["지역명", "연도", "분양가"]][:10]
res = df.loc[df["지역명"] == "서울",["지역명", "연도", "분양가"]][-10:]
print(res)
'''

# 인텍스 지정 선택
'''
df0 = df.cpoy()
print(df0)

# res = df.iloc[2]
res = df.iloc[2][4]
print(res)

res = df[df.index > 3500]
print(res)
'''

# 인덱스 필터
'''
res = df[df.index > 3560]
print(res) 
'''

# 필터
'''
res = df[df.연도 == 2023]
res = df[df.월 == 3]
print(res)
'''

# 비트연산 필터
'''
# res = df[(df.연도 == 2023) & (df.지역명 == "서울")]
# res = df[(df.연도 == 2023) & (df.지역명 == "서울")]
res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
print(res)
'''

# 컬럼 추가
'''
columns=list(df.columns)
print(columns)

# df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
df1 = df.reindex(columns=list(df.columns) + ["extra"])
print(df)
print("\n---------------------\n")
print(df1)

print("\n---------------------\n")
# df1.loc[:6, "extra"] = "0"
df1.loc[:4, "extra"] = False
print(df1)

# 복사
df2 = df1.copy()

# NaN 행 제거
# res = df2.dropna(how = "any")
# res = df2.fillna(value = True)
# res = df2.fillna(value = "1234")
# print(res)
res = df2.dropna(value = "1234", inplace = True)
print(df2)
print("\n---------------------\n")
res = df2.dropna(how = "any", inplace = True)
print(res)
print("\n---------------------\n")
print(df2)

# NaN 데이터 출력
# res = pd.isna(df1)
# res = pd.isna(df)
# res = pd.isna(df0)
res = pd.isna(df2)
print(res)

# 데이터 종류별 출력
# res = df["연도"].value_counts()
# res = df["지역명"].value_counts()
# res = df["월"].value_counts()
res = df.월.value_counts()
print(res)

# 그룹핑
# res = df.groupby(["지역명", "연도", "월"]).sum()
res = df.groupby(["지역명", "연도", "월"]).all()
print(res)

res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")
print(res)
'''
"""