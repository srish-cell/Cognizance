import numpy as np
n=int(input("Enter the size of the array: "))
A=np.array([])
B=np.array([])
print("Enter the values for Array A")
for i in range (n):
    print("A[",i,"] =\t")
    A=np.append(A,int(input()))
print("Enter the values for Array B")
for i in range (n):
    print("B[",i,"] =\t")
    B=np.append(B,int(input()))
print("First Array: \n",A)
print("Second Array: \n",B)
if (np.array_equal(A,B))==True:
    print("True")
else:
    print("False")

