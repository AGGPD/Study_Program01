#   DataType: int, float, str, list, dict, tuple, set, bool
'''
files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt", "f5.txt"]
print("files[0] ", files[0])
print("files[3] ", files[3])
print("files[-1] ", files[-1])
print("files[-3] ", files[-3])
'''


File = []
for i in range(5):
    File.append("F"+str(i+1)+".txt")
    print("has added file", File[i])

for i in range(len(File)):
    print("pop file", File.pop())
    print("remaining files", File)

files = ["f1.txt", "f2.txt"]

# 扩充入另一个列表
files.extend(["f3.txt", "f4.txt"])
print("extend", files)

# 按位置添加
files.insert(1, "file5.txt")     # 添加入第1位（首位是0哦）
print("insert", files)

# 移除某索引
del files[1]
print("del", files)

# 移除某值 
files.remove("f3.txt")
print("remove", files)


files = {"ID": 111, "passport": "my passport", "books": [1,2,3]}

# 按key拿取，并在拿取失败的时候给一个设定好的默认值
print('files["ID"]:', files["ID"])
print('files.get("ID"):', files.get("books", "不存在这个 ID")) # dict.get(key, default)

# 将另一个字典补充到当前字典
files.update({"books": ["3", "4"]})
print('update:', files)

# pop 调一个item，和列表的 pop 类似
popped = files.pop("ID")
print('popped:', popped)
print("remain:", files)