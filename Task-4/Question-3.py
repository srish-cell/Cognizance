#This is a program to create a two-dimensional list
n = int(input("Enter the number of phones you have: "))
list=[["Sno","Brand","Model"]]
for i in range (n):
    sno=i+1
    brand_name =input("Enter the name of the phone's brand: ")
    model =input("Enter the phone's model: ")
    list.append([sno,brand_name,model])
for i in list:
    for j in i:
        print(j,end='\t')
    print()
print("Second record of the list is")
for i in list[2]:
    print(i,end='\t')
#Alternative method
print("Alternative method")
w=int(input("Enter the number of columns: "))
h=int(input("Enter the number of rows: "))
list=[[0 for j in range(w)]for i in range (h)]
for i in range (h):
    if i==0:
        print("Enter the headings for the columns")
    else:
        print("Enter the values for the row", i + 1)
    for j in range (w):
        list[i][j]=input()
for i in list:
    for j in i:
        print(j,end='\t')
    print()
print("Second record of the list is")
for i in list[2]:
    print(i,end='\t')
