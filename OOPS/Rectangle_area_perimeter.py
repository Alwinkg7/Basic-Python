l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b


    def area(self):
        self.area = self.length * self.breadth
        print(self.area)
    def perimeter(self):
        self.perimeter = 2 * (self.length + self.breadth)
        print(self.perimeter)


obj1 = Rectangle(l,b)
obj1.area()
obj1.perimeter()