'''
try:
    with open("no_file.txt") as f:
        print(f.read())
except FileNotFoundError as e:
    print("error:", e)
    with open("no_file.txt", "w") as f:
        f.write("I am no_file.txt")
    print("file created")


d = {"name": "John", "age": 30}
l = [1,2,3]

try: 
    v = d["gender"]
    l[3] = 4
except KeyError as e:
    print("key error for dictionary:", e)
    d["gender"] = "X"
except IndexError as i:
    print("index error for list:", i)
    l.addpend(4)
print(d)
print(l)

l = [1,2,3]
try:
    l[3] = 4
    ddd= dddddd
except IndexError as e:
    print("index error:", e)
else :
    print("no error")
finally:
    print("I know there is error, so what?")
'''



