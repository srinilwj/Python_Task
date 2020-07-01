#Lucky number is 10
counter = 1
while counter <= 5:
    print("Attempt ", counter, ":")
    numb = int(input("Guess the number: "))
    if numb == 10:
        print("Good guess! \n")
        break
    else:
        if counter < 5:
            print("Try again! \n")
        else:
            print("Sorry but that was not very successful \n")
            break
    counter += 1

print("Game over!")