
import numpy as np
arr_1=np.array([[1,12,34],[20,10,21]])
print("First array: \n",arr_1)
arr_2=np.array([[9,8,5],[15,18,3]])
print("Second array: \n",arr_2)
Sum=np.add(arr_1,arr_2)
print("Sum of the two arrays: \n",Sum)
print("Array Redimensioning")
Array=np.vstack((arr_1,Sum))
print("Array: \n",Array)
x=int(input("Enter the no of rows: "))
y=int(input("Enter the number of columns: "))
Array=Array.reshape(x,y)
print(Array)
#Identity matrix
I=np.eye(3)#{Array with dimensions nxn}
print("Identity Matrix: \n",I)