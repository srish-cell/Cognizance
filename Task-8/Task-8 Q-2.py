import numpy as np
A=np.array([1, 0, 0, 0, 1, 0])
B=np.array([0, 0, 1, 1, 0, 1])
print("First Array: \n",A)
print("Second Array: \n",B)
if (np.array_equal(A,B))==True:
    print("True")
else:
    print("False")

