# 타이타닉 정보
"""
import pandas as pd
tr = pd.read_csv("data/train(12_1).csv")

'''
print(tr)
print("\n---------------------\n")
print(tr.head())
'''

'''
res = tr.isnull().sum()
print(res)
'''

# 승선지별 생존자
'''
res = pd.crosstab(tr["Embarked"], tr["Survived"])
print(res)

res.columns.map({0:"Dead", 1:"Alive"})
print(res)
'''

# 연령대별 생존자
'''
res = pd.crosstab(tr["Age"], tr["Survived"])
print(res)

res.columns.map({0:"Dead", 1:"Alive"})
print(res)
'''

# 승차등급별 생존자
'''
res = pd.crosstab(tr["Pclass"], tr["Survived"])
print(res)
'''

# 성별별 생존자
'''
res = pd.crosstab(tr["Sex"], tr["Survived"])
print(res)
'''

# 호칭별 (Allen, Mr. William Herry)
'''
tr["Title"] = tr.Name.str.extract(" ([A-Za-z]+)\.")
res = tr["Title"].value_counts()
print(res)

tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
tr["Title"] = tr["Title"].replace("Mlle", "Miss")
tr["Title"] = tr["Title"].replace("Mme", "Mrs")
tr["Title"] = tr["Title"].replace("Ms", "Miss")
res = tr["Title"].value_counts()
print(res)

print(tr["Age"].isnull())
print(tr["Age"].isnull().sum())
'''

# 그룹별 평균 나이
'''
meanAge = tr[["Title", "Age"]].groupby(["Title"]).mean()
print(meanAge)
print(tr["age"].head(20))

# 빈 나이 평균값 채워넣기
for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Title == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0]
    
print(tr["Age"].isnull())
print(tr["Age"].isnull().sum())
'''

# 나이 구간 나누기
'''
tr["FareCate"] = pd.qcut(tr.Age, 8, labels=range(1, 9))
print(tr.head())

print("\n---------------------\n")

print(tr.dtypes)

tr.AgeCate = tr.AgeCate.astype(int)
print(tr.head())
print(tr.dtypes)
'''

# 방번호별 탑승자
'''
tr.Cabin.fillna("N", inplace = True)
tr["CabinCate"] = tr["Cabin"].str.slice(start=0, stop=1)
print(tr["CabinCate"].value_counts())
'''

# 방번호 매핑
'''
tr["CabinCate"] = tr["CabinCate"].map({ "N": 0, "C": 1, "B": 2, "D": 3, "E": 4, "A": 5, "F": 6, "G": 7, "T": 8 })
tr.CabinCate = tr.CabinCate.astype
print(tr.dtypes)
print(tr)
print(tr["CabinCate"].value_counts())
'''

# 방번호별 생존자
'''
res = pd.crosstab(tr["CabinCate"], tr["Survived"])
print(res)
'''

# 요금컬럼 별 구간 구분
'''
print(tr.Fare)

print("\n---------------------\n")

print(tr["Fare"].value_counts())

tr["FareCate"] = pd.qcut(tr.Fare, 8, labels=range(1, 9))
# tr["FareCate"] = pd.qcut(tr.Fare, 5, labels=range(1, 9))
tr.FareCate = tr.FareCate.astype(int)
print(tr["FareCate"].value_counts())
'''

# 요금 구간별 생존자 
'''
res = pd.crosstab(tr["CabinCate"], tr["Survived"])
print(res)
'''
"""

# 아이리스 정보 처리
"""
import pandas as pd
df = pd.read_csv("./data/Iris(12_1).csv", index_col="Id")

print(df.head())

# 컬럼 매칭

df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
    inplace=True
)

ir = df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
    inplace=True
)

# print(ir.head())

# 컬럼 선택
'''
res = ir.iloc[:, [0, 1, 4]]
print(res)
'''

# 공통 string 제거
'''
ir["품종"] = ir["품종"].str[5:]
print(ir)
'''

# 그룹핑
'''
res = ir.groupby("품종").mean()
print(res)

res = ir["품종"].value_counts()
print(res)
'''
"""

# 데이터 시각화
"""
import matplotlib.pyplot as plt

# y축 데이터 지정 구성
'''
value = [1, 2, 3, 4]
# value = [2, 4, 5, 7, 10]
res = plt.plot(value)
plt.show()
'''

# x, y축 두 축 지정 구성
'''
x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

plt.plot(x_value, y_value)
# plt.plot([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
plt.show()
'''

# 딕셔너리 설정
'''
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.show()
'''

# 레이블 설정
'''
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data")
# plt.xlabel("y_data")
plt.ylabel("y_data")
plt.show()
'''

# 레이블 여백 조절 / 위치 조절
'''
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data = dic_val)

# plt.xlabel("x_data", labelpad = 15)
# plt.ylabel("y_data", labelpad = 50)

# plt.xlabel("x_data", labelpad = 10, loc="right")
# plt.ylabel("y_data", labelpad = 10, loc="top")

plt.xlabel("x_data", labelpad = 10, loc="left")
plt.ylabel("y_data", labelpad = 10, loc="bottom")

plt.show()
'''

# 다중데이터 출력
'''
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)
# plt.plot ([1,4,5,9], [2,3,8,10])

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.show()
'''

# 라벨 출력
'''
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")

plt.legend()
plt.show()
'''

# 위치 조절 
'''
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

# plt.plot("x_data", "y_data", data = dic_val)

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.xlabel("x_data")
plt.ylabel("y_data")

# plt.legend()
# plt.legend(loc = (1, 1))
# plt.legend(loc = "best")
# plt.legend(loc = (0.5, 0.5))
# plt.legend(loc = (0.3, 0.3))

# plt.legend(loc="lower right")
# plt.legend(loc="center right")
# plt.legend(loc="upper right")
# plt.legend(loc="lower left")
plt.legend(loc="enter left")

plt.show()
'''

# 라벨 설정
'''
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic_val = {"x_data": [1,3,5,7,9], "y_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.plot("x1_data", "y1_data", data=dic_val, label="PData(km)")
# plt.plot ([1,4,5,9], [2,3,8,10])
plt.xlabel("x_data")
plt.ylabel("y_data")

# col 조절
# plt.legend(ncol = 1)
# plt.legend(ncol = 2)

# 콘트 조절
plt.legend(ncol = 2, fontsize = 10)
plt.legend(ncol = 2, fontsize = 20)

# 테두리 설정
# plt.legend(ncol = 2, fontsize = 20, frameon = True)
# plt.legend(ncol = 2, fontsize = 20)
# plt.legend(ncol = 2, fontsize = 20, frameon = False)


# 테두리 음영 설정
# plt.legend(ncol=2, fontsize=20, shadow=True)

plt.show()
'''

# 축 범위 지정
'''
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)
plt.xlabel("x_data")
plt.ylabel("y_data")

# plt.xlim()
# plt.ylim()

# 축 범위 출력
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
print(x_min, x_max)
print(y_min, y_max)

# 축 계산
# plt.xlim(x_min - 0.6, x_max)
# plt.ylim(y_min - 0.6, y_max)

# 축 범위 지정
# plt.xlim([0, 10])
# plt.ylim([0, 10])
# plt.axis([0, 10, 0, 10])

# plt.xlim([0, 50])
# plt.ylim([0, 50])
# plt.axis([0, 50, 0, 50])

# plt.xlim([-5, 50])
# plt.ylim([-5, 50])
# plt.axis([-5, 15, -5, 50])

# 두축 값 동시 확인
# x_min, x_max, ymin, ymax = plt.axis()

# 두 축을 동시 지정
# print(x_min, x_max, ymin, ymax)
# plt.axis(x_min, x_max, ymin, ymax)

# 축 출력 옵션 지정
# plt.axis("square")
# plt.axis("scaled")
# plt.axis("equal")
# plt.axis("tight")
# plt.axis("auto")
# plt.axis("on")
# plt.axis("off")

# 선 스타일 설정

# plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

# plt.plot([2,3,6,7,10], [1,4,5,8,9], "- -", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ":", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "-.", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ",", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label="PData(km)")

# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")

plt.show()
'''
"""