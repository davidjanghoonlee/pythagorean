# Pythagorean Theorem a^2 + b^2 = h^2 , (where 'h' is the hypotenuse)
#importing 'sys' and 'string' module from python
import sys,string

def rerun():
    pythagorean()

def pythagorean():
    #First of all, print the question.
    print "Which side is unknown? \n"

    # Print choices for the question.
    print ("1. Side 1")
    print ("2. Side 2")
    print ("3. hypotenuse")
    print ("4. Quit\n")

    #Choice function: Let the user type his / her choice
    choice = input("Type your Choice 1/2/3/4: ")

    #If the choice is 1, the program will do these things.
    if choice == 1:
        #let the user type the two sides that he / she knows
        h = float(input("Insert the length of the hypotenuse: "))
        b = float(input("Insert the length of side 2: "))
        #calculate and print the result
        print "The length of Side 1 is: " ,(h**2 - b**2)**0.5 ,".\n"
        rerun()

        #If the choice is not 1 but 2, the program will do these things
    elif choice == 2:
        #let the user type the two sides that he / she knows
        h = float(input("Insert the length of the hypotenuse: "))
        a = float(input("Insert the length of side 1: "))
        #calculate and print the result
        print "The length of Side 2 is: " ,(h**2 - a**2)**0.5 ,".\n"
        rerun()

        #If the choice is neither 1 nor 2 , the program will
    elif choice == 3:
        #let the user type the two sides that he / she knows
        a = float(input("Insert the length of side 1: "))
        b = float(input("Insert the length of side 2: "))
        #calculate and print the result
        print " The length of the hypotenuse is: " ,(a**2 + b**2)**0.5, ". \n"
        rerun()

        #if the choice is neither
    elif choice == 4:
        #this function from 'sys' module closes the file
        sys.exit(0)
    else:
        print "Invalid Option. Please Try Again."
        rerun()


pythagorean()
