#write a program to take  a user age and
#let him know if he can go to club
#21
#logic building formula

#step 1
#i/p - age,int
#o/p -string( can go to club or not)
#step 2 - Rough logic
# age>21 =->print can go
#age<21 = print cant go

#step 3 - write logic
age = int(input("Enter your age:\n"))
if age >= 21:
    print("you can go")
else:
    print("you can not go")

#Step 4. Check for the edge cases
#We should consider edge casessuc as:
#Negative ages or exteremly high values -> program will break
#Non- numeric input - ABC
#Age which is valid>130
#Step 5. Optimize the code.
#Handle all the edge



