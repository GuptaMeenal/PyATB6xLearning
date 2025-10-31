#Write a program to calculate the area of circle give its redius using formula
#area =3.14*r^2
#i/p - r - float
# o/p - string formatted output of area
import math

r = float (input("enter radius"))
area = math.pi*(pow(r,2))
print(area)

#strint data formatting
print(f"area ofcircle is ->{area :.2f}")
