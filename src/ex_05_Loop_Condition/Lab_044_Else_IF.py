#Find a  postive number is even or odd
num = int(input("Enter a number: ").strip())
if num>0:
 print( "Even"if num%2==0 else 'Odd')
    #if num % 2 == 0:
      #print(even)
    #else:
        #print("Odd")

else:
    print("The number is negative")


    #you can wrtie short one liner conditions using ternary operator