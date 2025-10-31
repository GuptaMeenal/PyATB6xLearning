#Grade Calculator:
#write a program the calculates and display the letter grade
#For a given numerical score (e.g: A,B,C,D,F)
#A: 90-100
#B:80-89
#C: 70-79
#D: 60-69
#F: 0-59

#Logic building formula
#1 -> Input - Int
#2->output - str ->A,B
Score = int(input("Enter the score: ").strip())
#if 0 < Score < 100:    #Simplified chaining
"""
if (Score >= 0 and Score >= 100):
    print("❌Enter valid score❌",Score)
else:
    print("Let me check")
"""
if Score <= -1 or Score >= 100 :
    print("❌you are super man!!, you cant get a grade!!")
else:
    if Score >= 90 and Score < 100:
        print("Your grade is A")
    elif Score >= 80 and Score < 90:
        print("Your grade is B")
    elif Score >= 70 and Score < 80:
        print("Your grade is C")
    elif Score >= 60 and Score < 70:
        print("Your grade is D")
    else:
        print("Your grade is F")




