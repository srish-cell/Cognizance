#This program is to determine whter a given number is a palindrome or not
num=int(input("Enter a number: "))
x=num
rev=0
while x>0:
    rem=x%10
    rev=rev*10+rem
    x=x//10
if (rev==num):
    print("True")
else:
    print("False")