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

print("\n---------------------\n")
print(df.name == "김서윤")

print("\n---------------------\n")
print(df.company == "유한회사")

print("\n---------------------\n")
temp = df[df.postcode > 70000]
print(temp)

print("\n---------------------\n")
res = df[df.color == "DarkKhaki"].head(3)
print(res)

print("\n---------------------\n")
res = df[df.postcode > 70000][["name", "postcode"]]
print(res)
print(res.count)

print("\n---------------------\n")
temp = df.postcode.mean()
print(temp)

print("\n---------------------\n")
temp = df.postcode.sum()
print(temp)

print("\n---------------------\n")
temp = df[df.color == "DarkKhaki"].postcode.mean()
print(temp)

print("\n---------------------\n")
temp = df[df.color == "DarkKhaki"].postcode.sum()
print(temp)

print("\n---------------------\n")
temp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
print(temp)

print("\n---------------------\n")
temp = df[df.postcode > df.postcode.mean()]
print(temp)

print("\n---------------------\n")
temp = df.company.isnull()
print(temp)

print("\n---------------------\n")
# temp = df.temp.empty
temp = df.company.empty
print(temp)

print("\n---------------------\n")
temp = df[df.company.isnull()][["name", "postcode"]]
print(temp)

print("\n---------------------\n")
temp = df.company.isnull()
for el in temp:
    if el == True:
        print(el)

print("\n---------------------\n")
temp = df.name.empty
print(temp)

print("\n---------------------\n")
temp = [df.company.isnull()][["name", "postcode"]]
print(temp)

print("\n---------------------\n")
temp = df[df.color == "DarkKhaki"]
print(temp)

print("\n---------------------\n")
temp = df[~(df.color == "DarkKhaki")]
print(temp)
# print(temp.count)

print("\n---------------------\n")
temp = df[~(df.color == "DarkKhaki")][["name"]]
print(temp)

print("\n---------------------\n")
temp = df[(df.color == "DarkKhaki") & (df.postcode > 70000)]
print(temp)

print("\n---------------------\n")
temp = df[(df.color == "DarkKhaki") | (df.postcode > 70000)]
print(temp)

print("\n---------------------\n")
temp = df[(df.color == "DarkKhaki") | (df.postcode > 70000)][["name", "postcode"]]
print(temp)

print("\n---------------------\n")
temp = df.sort_values("postcode")
print(temp)

print("\n---------------------\n")
temp = df.sort_values("postcode", ascending = False)
print(temp)

print("\n---------------------\n")
temp = df.sort_values("name", ascending = False)
print(temp)
'''
"""

# 데이터 재배열
"""
import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

print("\n---------------------\n")
# print(df.pivot())
print(df.pivot(index='Machine',columns='Country',values='Price'))
# print(df.pivot(index='Brand',columns='Machine',values='Price'))
# print(df.pivot(index='Country',columns='Machine',values='Price'))
# print(df.pivot(index='Price',columns='Brand',values='Machine'))
"""