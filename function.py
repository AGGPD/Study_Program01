from datetime import datetime

'''
# 1. Create a class called File
class File:
    def __init__(self, name, create_time = None):
        self.name = name
        self.create_time = create_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    def get_info(self):
        return f"{self.name} is created at {self.create_time}"

my_file = File("my_file.txt")
print(my_file.get_info())

# 2. Create a class called Video that inherits from File
class File:
    def __init__(self, name, create_time = "today"):
        self.name = name
        self.create_time = create_time

    def get_info(self):
        return f"{self.name} is created at {self.create_time}"

class video(File):
    def __init__(self, name, windows_size = (1080, 720)):
        super().__init__(name = name, create_time = "today")
        self.windows_size = windows_size

class Text(File):
    def __init__(self, name,language = "zh-cn"):
        super().__init__(name = name, create_time = "today")
        self.language = language
        
    def get_more_info(self):
        return self.get_info() + ", using language of " + self.language

v = video("my_video.mp4")
t = Text("my_text.txt")
print(v.get_info())
print(t.create_time)
print(t.language)
print(t.get_more_info())
'''

class File:
    def __init__(self):
        self.name = "f1"
        self.__deleted = True  # 我不让别人用这个变量
        self.__type = "txt"      # 我不想别人使用这个变量
    
    def delete(self):
        self.__force_delete()
    
    def __force_delete(self):  # 我不让别人使用这个功能
        self.__deleted = True
        return True
        
    def _soft_delete(self):     # 我不想让别人使用这个功能
        self.__force_delete()   # 我自己可以在内部随便调用
        return True

f = File()
print(f.__type)      # 可以拿到值，但是这个类的作者不想让你直接这样拿到# 可以调用，但是这个类的作者不想让你直接调用