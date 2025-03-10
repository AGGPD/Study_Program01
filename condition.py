# Description: This file is used to demonstrate the use of conditional statements in Python.
'''trash = True
if in_trash:
    print('This file is in the trash.')
else:
    print('This file is not in the trash.')


# The following code is used to demonstrate the use of if-else statements in Python.
a, b = 1, 2
if a > b:
    print("a 大于 b")
else:
    print("a 不大于 b")

# The following code is used to demonstrate the use of if-elif-else statements in Python.
today = 4
if today == 1:
    print("周一")
elif today == 2:
    print("周二")
elif today == 3:
    print("周三")
else:
    print("周一周二周三之外的一天")



# The following code is used to demonstrate the use of comparison operators in Python.
print("2 < 3", 2 < 3)
print("3 < 2", 3 < 2)
print("2 != 2", 2 != 2)
print("2 == 2", 2 == 2)


# The following code is used to demonstrate the use of logical operators in Python.
print(2 < 3 and 2 < 5)
print(2 > 3 or 3 == 3)
print(2 > 3 or not 3 == 3 and 5 < 10)


print(3 ** 3)
print(2.5 ** 2)
print(1 ** 2)
print(1.5 ** 1.5)
'''
for i in range(10):
    if i % 2 == 0:
        continue # 跳过偶数
    print(i)


count = 0
guess_num = 10
while guess_num != 20:
    guess_num += 1
    count += 1
    if count > 5:
        break
    print(guess_num)