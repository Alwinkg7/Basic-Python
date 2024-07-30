#inheritance

class person:    #main class
    def function1(self):
        print("Inside person function")
class child(person):   #sub class
    def function2(self):
        print("Inside child function")

obj = person()
obj.function1()
obj = child()
obj.function2()


