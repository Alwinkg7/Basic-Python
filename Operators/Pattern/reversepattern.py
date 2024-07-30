n = int(input("Enter the number of rows: "))

for i in range(n,0,-1):  #range (5+1,0,-1)
    for j in range(i):   #range (0,5)
        print(i, end=" ")
    print()