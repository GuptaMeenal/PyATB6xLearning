#step 1
#i/p - age,int
#o/p -string( can go to club or not)
#step 2 - Rough logic
# age>21 =->print can go
#age<21 = print cant go

#step 3 - write logic
age = int(input("Enter your age:\n".strip()))
if age<= 0 or age<130:
    print("Enter a valid age.")
else:
   if age >= 21:
    print("you can go")
   else:
    print("you can not go")

#Strip - will remove extra spaces from input function
