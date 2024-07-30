"""
    print("hello world")
    x = 10
    print(x)"""
class myclass:
    def __init__(self,name, age):
        self.your_name = name
        self.your_age = age
    def displaydata(self):
        print("Name: ",self.your_name)
        print("Age: ",self.your_age)

obj = myclass("alwin",55)
obj1 = myclass("alwi",5)
obj.displaydata()
obj1.displaydata()