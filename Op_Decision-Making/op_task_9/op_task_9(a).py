#PART 1, Lucky number is 7
user_guess = int(input("Guess the lucky number: "))

while True:
    if user_guess == 7:
        print("Congratulations! You've nailed it! :)")
        break
    else:
        print("Oops sorry,  no luck this time \n")