#factorial of 5 is 5*4*3*2*1 = 120
num = int(input("Enter a number for which factorial is: "))
factorial = 1
if num <= 0:
    print("Factorial",factorial)
else:
    for i in range(1,num + 1):
        factorial = factorial * i
    print("Factorial of",num,"is",factorial)
