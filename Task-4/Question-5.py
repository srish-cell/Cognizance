#Print a equilateral triangle pattern using "*"
n=5 #( Number of rows = n, we can use int(input(..)) function to get the input from user also)
for i in range (n):
    for j in range (n):
        print(end=" ")
    n=n-1
    for p in range (i+1):
        print("*",end=' ')
    print(" ")

#Alternative method/code
n=5
print("Alternative Method")
for i in range (n) :
    print(" "*(n-i-1),end=" ")
    print("* "*(i+1))
