#Problem find max between 3 numbers.
#logic
#user input - num1 ,num2 ,num3
#o/p int or string with max number
#Logic

num1 = float(input("Enter the first number: ")) #5 ,#10
num2 = float(input("Enter the second number: ")) #3 ,#12
num3 = float(input("Enter the third number: ")) #2 ,#11

#5>2 and 5>3 ->5
#num1 >num2 and num1> num3 -> num1
#num2>num1 and num2>num3 -> num 2
#num 3 max

if num1 >= num2 and num1 >= num3:
    print("max",num1)
elif num2>=num1 and num2>=num3:
    print("max",num2)
else:
    print("max",num3)

