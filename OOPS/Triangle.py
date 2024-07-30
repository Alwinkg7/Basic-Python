a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))

class triangle:
    def __init__(self,a,b,c):
        self.a=A
        self.b=B
        self.c=C
    def area(self):
        area =(self.b**2) - (4*a*c)
        print("The area of the triangle is:",area)
        return area

tri=triangle(a,b,c)
tri.area()