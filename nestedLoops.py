#introduction to nested loops in python
#inner loop goes first before outter loop

n = int(input("What is the number of rows?: "))
m = int(input("What is the number of columns: "))
ANM = input("Enter a symbol to use for matrix representation: ")

for i in range(n):
    for j in range(m):
        print(ANM, end="")
    print()
