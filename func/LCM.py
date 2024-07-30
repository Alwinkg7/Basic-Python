#LCM
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
def LCM(a, b):
    if a > b:
        largest = a
    else:
        largest = b
    while (True):
        if (largest % a == 0 and largest % b == 0):
            lcm = largest
            break
        largest = largest + 1
    return lcm
print(LCM(a, b))