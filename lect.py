"""
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)  

"""

"""
a = 5
b = 5

print(a is b)
print(a is not b)
"""

"""
a = 3
b = 3.0

print(a == b)
print(a is b)
print(a is not b)
"""

"""
a = [3, 5, 1]
b = a

print(a is b)

a[0] = 2

print(a, b)

print(a is b)
"""

"""
#a = 2 + 3 * 4
#a = 10 / 5 / 2
#a = 2 ** 3 ** 2
#a = 10 % 3 % 2
#a = 1 + 2 > 3 and 4 - 1 < 2
#a = not False and True
#a = not True or False and True
#a = 1 & 2 | 3 ^ 4
#a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
#a = 2 * -3 // 2
#a = 1 == 2
#a = 1 == 2 != 3

print(a)
"""

"""
#x = 0
#x = 1
#x = -1

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
"""


# if 짝수, 홀수
"""
num = 23
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
"""

# if 두수 비교
"""
a = 2
b = 3
if a == b:
    print("같아요")
else:
    print("달라요")
"""


# if a or b 인지
"""
clear = "a"
if clear == "a" or clear == "b":
    print("'a' 또는 'b' 입니다.")
else:
    print("'a' 또는 'b'가 아닙니다.")
"""

# for 예시
"""
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
"""

# 이중 For 문 출력
"""
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)
"""

# for 0 ~ 9 출력

"""
for i in range(10):
    print(1)
"""
# for 역순출력 reversed

"""
for char in "Python":
    print(char)
"""

# for 역순출력 reversed
"""
fruits = ["apple", "banana", "cherry"]

for fruit in reversed(fruits):
    print(fruit)
"""

# for 역순출력 sorted
"""
fruits = ["apple", "banana", "cherry"]

for fruit in sorted(fruits, reverse = True):
    print(fruit)
"""

# for 구구단
"""
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
"""

# for else 예문
"""
rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
else :
	print("end process")
"""

"""
for i in range(10):
    if i == 7:
        print("break", i)
        break
    elif i == 1:
        print("continue", i)
        continue
    else:
        print("pass", i)
        pass

    print(i)
"""

# while 1 ~ 5 출력
"""
i = 1

while i <= 5:
    print(i)
    i += 1
"""

# while 0 ~ 9 출력
"""
i = 0

while i <= 9:
    print(i)
    i += 1
"""

# while 문자열 낱자 출력
"""
str_word = "python"
i = 0

while i < len(str_word):
    print(str_word[i])
    i += 1
"""

# while 1 ~ 10 총합
"""
sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1
    
print(sum)
"""

# while 1 ~ 100 짝수, 홀수 출력
"""
i = 1

while i <= 100:
    if i % 2 == 0:
        print("짝수 :", i)
    elif i % 2 == 1:
        print("홀수 :", i)
    i += 1
"""

# while 1 ~ 100 7의 배수만 출력
"""
i = 1

while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1
"""