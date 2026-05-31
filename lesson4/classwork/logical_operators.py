age = int(input("What is your age madam!"))
ticket = (input("Buddy do you have a ticket yes/no"))
if age>= 13 and ticket == "yes":
    print("You may enter")
else:
    print("Get out of here you cannot come!!!!!!!!")


hs = (input("Do you have a bus pas yes/no"))
c = (input("Do you have spare money yes/no"))
if hs=="yes" or c=="yes":
    print("You may come in")
else:
    print("You are not coming in my bus!!!!!")

home =(input("Did you do your homework yes/no"))#not does the opsosite
if not home == "yes":
    print("Go do your homework!")
else:
    print("Good job you win the lottery of 1000000000000 dollars!!!!!!From doing your homework!")
#You can combine logical operrators
sh = (input("Do you have a permission slip yes/no"))
bh = (input("Are you sick yes/no"))
lh = (input("do you have a shaperon"))
if sh == "yes"and not bh=="no" and lh=="yes":
    print("You may go on the billion dollar field trip!!!")
elif bh == "yes":
    print("Rest")
else:
    print("You need to have both a permission slip and a shaperon to go on the field trip")