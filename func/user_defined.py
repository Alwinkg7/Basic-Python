#user defined
"""def myfunc():
    print("Hello World")
    print("I am a function")
myfunc()"""

"""
#required
def Square(language):
    print("programming",language,)
Square("python")
Square("HTML")
Square("C++")
Square("Java")
Square("C#")
Square("Javascript")
Square("PHP")
Square("Ruby")"""

"""
#keyword arguement
def myfunc(name,age,place):
    print("Name: ",name)
    print("Age: ",age)
    print("Place: ",place)
myfunc("David",12,"tcr")
myfunc("Davi",21,"calicut")
myfunc("David","malapuram",23)
myfunc("Aliwn",place="kollam",age=50) #keyword arguement
"""
"""
#default arguement
def myfunc(name,age,place="tcr"):
    print("Name: ",name)
    print("Age: ",age)
    print("Place: ",place)
myfunc("David",12,)
myfunc("Davi",21,)
myfunc("David","malapuram",23)
"""
"""
#variable arguement
def myfunc(name, *args):
    print("Name: ",name)
    print(args)
myfunc("David")
myfunc("anmi","lala",1,5,3,6,4)"""
"""
#Return statment
num = int(input("Enter a number: "))
def Square(num):
    return num*num
print("Square of the given number is = ",Square(num))"""

#Arithematic operation using function

def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
def power(num1,num2):
    return num1**num2

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Exit")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
choice=int(input("Enter your choice: "))
if choice==1:
    print("Addition")
    print("Addition of both numbers is = ",add(x,y))
elif choice==2:
    print("Subtraction")
    print("Subtraction of both numbers is = ",subtract(x,y))
elif choice==3:
    print("Multiplication")
    print("Multiplication of both numbers is = ",multiply(x,y))
elif choice==4:
    print("Division")
    print("Division of both numbers is = ",divide(x,y))
elif choice==5:
    print("Power")
    print("Exponentiation of both numbers is = ",power(x,y))
elif choice==6:
    print("Exit")
else:
    print("Invalid choice")
    print("Please try again")
