#for i in range(12):
    #first range(start,end,step)
    #second starting value default =0
    #third step value default = 1
    #print(i)

""""n = int(input("Enter a number: "))
for i in range(n,(n*10)+1,n):  #first number is the given num second is set of num(1-10) third is multiplicant
    print(i)"""

"""celsuis = float(input("Enter the temperature in Celsius: "))
farenheit = celsuis * 9 / 5 + 32
print("Celsius is converted to Farenheit = ",farenheit)"""

""" #prime or not
num = int(input("Enter a number: "))
if num > 1: #check if number is greater than 1
    for i in range(2, num):
        if num % i == 0:
            print(num,"is not prime")
            break
    else:
        print(num,"is prime")"""

#Factorail
print("To find Factorial of a number")
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Enter a positive number")
elif num == 0:
    print(f"{num} is not a factorial")
else:
    for i in range(1,num+1): #(1,5)
       factorial = factorial*i #1*1=1 1*2=2 2*3=6 6*4=24 24*5=120
    print(f"Factorial of {num} : ", factorial)