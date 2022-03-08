import numpy as np
a=int(input("First number: "))
b=int(input("Last number: "))
c=np.linspace(a,b,b-a+1)
x=5
array=np.zeros(len(c)+(len(c)-1)*(x))
array[::x+1]=c
print(array)