#This program is to display the characters at even places from the string accepted from the user
a = input("Enter any string: ")
print(a[0::2])
#Alternative method 1
print("Alternative method 1")
b=0
for i in a:
    if (b%2==0):
        print(i,end='')
    b+=1
print("")
#Alternative method 2
print("Alternative method 2")
b=0
while b<len(a):
    if (b%2==0):
        print(a[b],end='')
    b=b+1

