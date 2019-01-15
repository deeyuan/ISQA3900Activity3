#Title
print ("ISQA 3900 Letter Grade Calculator")
print()

choice = "y" or "n"

while choice.lower() == "y":

    #get points
    points_earned = float (input("Enter total number of points earned:\t"))
    round (points_earned,2)

    if points_earned >=920 and points_earned <= 1000:
        grade = "A"
        print("Letter grade:", grade)
        choice = str(input("Continue (y/n)?:\t"))
    elif points_earned >= 880 and points_earned < 920:
        grade = "B+"
        print("Letter grade:", grade)
        choice = str(input("Continue (y/n)?:\t"))
    elif points_earned >= 820 and points_earned < 880:
        grade = "B"
        print("Letter grade:", grade)
        choice = str(input("Continue (y/n)?:\t"))
    elif points_earned >= 780 and points_earned < 820:
        grade = "C+"
        print("Letter grade:", grade)
        choice = str(input("Continue (y/n)?:\t"))
    elif points_earned >= 700 and points_earned < 780:
        grade = "C"
        print("Letter grade:", grade)
        choice = str(input("Continue (y/n)?:\t"))
    elif points_earned >= 600 and points_earned < 700:
        grade = "D"
        print("Letter grade:", grade)
        choice = str(input("Continue (y/n)?:\t"))
    elif points_earned <600 and points_earned >= 0:
        grade = "F"
        print("Letter grade:", grade)
        choice = str(input("Continue (y/n)?:\t"))
    else:
        print ("Points you entered is out of range. Please reenter\n")

#user choice to exit
while choice.lower () == "n":
    print ("Thank you for using the Letter Grade Calculator!")
    exit()

#user enter the insufficent choice and exit the app
while choice.lower () != "y" or "n":
    print ("Invalid entry. Thank you for using the Letter Grade Calculator")
    exit()