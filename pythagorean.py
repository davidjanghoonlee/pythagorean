# Pythagorean Theorem a^2 + b^2 = h^2 , (where 'h' is the hypotenuse)
#importing 'sys' and 'string' module from python
import sys,string
import time

#First of all, print the question.
while True:
    print "Which side is unknown? "

    # Print choices for the question.
    print ("1. Side 1")
    print ("2. Side 2")
    print ("3. hypotenuse")
    print ("4. Quit")

    #Choice function: Let the user type his / her choice
    choice = input("Type your Choice 1/2/3/4: ")

    #If the choice is 1, the program will calculate and return the value of side 1
    if choice == 1:
        #let the user type the two sides that he / she knows
        h = float(input("Insert the length of the hypotenuse: "))
        b = float(input("Insert the length of side 2: "))
        #calculate and print the result
        print "The length of Side 1 is: " ,(h**2 - b**2)**0.5 ,"."

    #If the choice is 2, the program will calculate and return the value of side 2
    elif choice == 2:
        #let the user type the two sides that he / she knows
        h = float(input("Insert the length of the hypotenuse: "))
        a = float(input("Insert the length of side 1: "))
        #calculate and print the result
        print "The length of Side 2 is: " ,(h**2 - a**2)**0.5 ,"."

    #If the choice is 3, the program will calculate and return the hypotenuse.
    elif choice == 3:
        #let the user type the two sides that he / she knows
        a = float(input("Insert the length of side 1: "))
        b = float(input("Insert the length of side 2: "))
        #calculate and print the result
        print " The length of the hypotenuse is: " ,(a**2 + b**2)**0.5, "."

    #If the choice is 4, the program will exit.
    elif choice == 4:
        print "Exiting the Program...\nThank You!\n Good Bye!"
        #delay 1 second to let the user read the printed farewell statement.
        time.sleep(1)
        #exit
        sys.exit(0)
    else:
        print "Invalid Option. Please Try Again."

#a = float(input("Insert the length of side 1: "))
#b = float(input("Insert the length of side 2: "))
#h = float(input("Insert the length of the hypotenuse: "))
