#PART 2, Lucky number is 7
number = int(input("Guess the lucky number: "))

while True:
    if number == 7:
        print("Congratulations! You've nailed it! :) \n")
        break
    else:
        print("Oops, no luck this time \n")
        answer = input("Do you want to try again? (Yes/No): ")
        if answer == "No":
            break
        else:
            number = int(input("Guess the lucky number again: "))