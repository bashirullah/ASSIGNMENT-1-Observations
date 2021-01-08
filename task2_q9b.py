Enter_Lucky_Num = input("Guess the lucky number ")
while Enter_Lucky_Num != 5:
    print "That is not the lucky number"
    number = input("Guess the lucky number ")


number = -1
again = "yes"
while number != 5 and again != "no":
    number = input("Guess the lucky number: ")
    if number != 5:
        print "That is not the lucky number"
        again = raw_input("Would you like to guess again? ")