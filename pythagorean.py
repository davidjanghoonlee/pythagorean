# Pythagorean Theorem a^2 + b^2 = h^2 , (where 'c' is the hypotenuse)
#a = side_1 / b = side_2 /  h = side_3

#First of all, give instructions
print "Which side is unknown? "

# what does the user want to know about?
print ("1. Side 1")
print ("2. Side 2")
print ("3. hypotenuse")

#Choice function
choice input(": ")

if choice == 1;
    b = int(input("Insert the length of side 2: "))
    h = int(input("Insert the length of the hypotenuse: "))
    print "The length of Side 1 is: " , (h^2 - b^2)^(1/2) ,"."
elif choice == 2;
    a = int(input("Insert the length of side 1: "))
    h = int(input("Insert the length of the hypotenuse: "))
    print "The length of Side 2 is: " , (h^2 - a^2)^(1/2) ,"."
elif choice == 3;
    a = int(input("Insert the length of side 1: "))
    b = int(input("Insert the length of side 2: "))
    print " The length of the hypotenuse is: " , (a^2 + b^2)^(1/2), "."
else:
    print "Invalid Option. Please Try Again."

#a = int(input("Insert the length of side 1: "))
#b = int(input("Insert the length of side 2: "))
#h = int(input("Insert the length of the hypotenuse: "))

def side_1 (b,h)
    return
