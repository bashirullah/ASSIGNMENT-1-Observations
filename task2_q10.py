counter = 1
while counter <= 5:
    number = input("Guess the " + str(counter) + ". number ")
    if number != 5:
        print( "Try again.")
        counter=counter+1
    else:
        print ("Good guess!")
        counter = counter +1
else:
    print ("Game over")
    