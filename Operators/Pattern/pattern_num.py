n = int(input("Enter number of rows: "))
#outer loop for managing number of rows
for i in range(n+1):
    #inner loop for managing number of cols
    for j in range(1,i+1):
        print(j,end="  ")
    print()