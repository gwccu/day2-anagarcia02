myName = "Anastasia"
print(myName)
myname = "Anastasia Garcia "
print(myname * 78)


#Here is the problem set.

userInteger = input("Pick any integer.")
if(int(userInteger) % 2 == 0):
    print("This integer is even.")
else:
    print("This integer is odd.")



userInteger_1 = input("Pick any integer.")
if(int(userInteger_1) % 2 == 0):
    print("This integer is even.")
else:
    userInteger_1 = 1

userInteger_2 = input("Pick any integer.")
if(int(userInteger_2) % 2 == 0):
    print("This integer is even.")
else:
    userInteger_2 = 1

userInteger_3 = input("Pick any integer.")
if(int(userInteger_3) % 2 == 0):
    print("This integer is even.")
else:
    userInteger_3 = 1

totalOdd = (int(userInteger_1 + userInteger_2 + userInteger_3))
print("You have picked" , str(totalOdd) , "odd integers.")


print("Let's conduct a test on your weirdness. Please only answer with yes or no.")
q1 = input("Do you like olives on your pizza?")
if q1 = "yes":
    q1 = 1
else: q1 = 0

q2 = input("Do you sleep with socks on?")
if q2 = "yes":
    q2 = 1
else: q2 = 0

q3 = input("Do you take a bath before a shower?")
if q3 = "yes":
    q3 = 1
else: q3 = 0

q4 = input("Do you talk to yourself?")
if q4 = "yes":
    q4 = 1
else: q4 = 0

q5 = input("Do you clap when the plane lands?")
if q5 = "yes":
    q5 = 1
else: q5 = 0

if(q1 + q2 + q3 + q4 + q5 == 5)
    print("You have a weirdness score of 5.  Weirdo.")
if(q1 + q2 + q3 + q4 + q5 == 4)
    print("You have a weirdness score of 4-- pretty weird.")
if(q1 + q2 + q3 + q4 + q5 == 3)
    print("You have a weirdness score of 3.")
if(q1 + q2 + q3 + q4 + q5 == 2)
    print("You have a weirdness score of 2.")
if(q1 + q2 + q3 + q4 + q5 == 1)
    print("You have a weirdness score of 1.")
if(q1 + q2 + q3 + q4 + q5 == 0)
    print("You have a weirdness score of 0.")