n = int(input("Enter number of rows: "))
#outer loop for managing number of rows
for i in range(0,n+1):
    #inner loop for managing number of cols
    for j in range(i):
        print(i,end="  ")
    print()