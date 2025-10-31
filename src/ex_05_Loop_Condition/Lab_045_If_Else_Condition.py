#problem yo find max between two.
#logic building formula
#1. user input ->two integers
#2. o/p - int 1 which ever is grater max number will return
#3.14 or 45.34 -float
num1   = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
#if num1>0 and num2>0:(if interview ask for positive number max)

if num1>=num2:
 print("Maximum",num1)
else:
 print("Maximum",num2)
#else:
#print("Negative",num1,num2)

#num1 ==num2 handled