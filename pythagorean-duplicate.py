# Pythagorean Theorem a^2 + b^2 = h^2 , (where 'h' is the hypotenuse)
import sys,string


#def l1(h,b):
#    return (h**2 - b**2)**0.5

#def l2(h,a):
    return (h**2 - a**2)**(1/2)

def hy(a,b):
    return (a**2 + b**2)**(1/2)

#First of all, print the question.
print "Which side is unknown? "

# Print choices for the question.
print ("1. Side 1")
print ("2. Side 2")
print ("3. hypotenuse")
print ("4. Quit")

#Choice function: Let the user type his / her choice
choice = input("Type your Choice 1/2/3/4: ")

#If the choice is 1, the program will do these things.
if choice == 1:
    #let the user type the two sides that he / she knows
    h = float(input("Insert the length of the hypotenuse: "))
    b = float(input("Insert the length of side 2: "))
    #calculate and print the result
    print "The length of Side 1 is: " ,(h**2 - b**2)**0.5 ,"."

#If the choice is not 1 but 2, the program will do these things
elif choice == 2:
    #let the user type the two sides that he / she knows
    h = float(input("Insert the length of the hypotenuse: "))
    a = float(input("Insert the length of side 1: "))
    #calculate and print the result
    print "The length of Side 2 is: " ,(h**2 - a**2)**0.5 ,"."

#If the choice is neither 1 nor 2 , the program will
elif choice == 3:
    #let the user type the two sides that he / she knows
    a = float(input("Insert the length of side 1: "))
    b = float(input("Insert the length of side 2: "))
    #calculate and print the result
    print " The length of the hypotenuse is: " ,(a**2 + b**2)**0.5, "."
elif choice == 4:
    sys.exit(0)
else:
    print "Invalid Option. Please Try Again."

#a = float(input("Insert the length of side 1: "))
#b = float(input("Insert the length of side 2: "))
#h = float(input("Insert the length of the hypotenuse: "))
