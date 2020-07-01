#Lucky number is 100 or 200
counter = 1
while counter <= 5:
    print("Attempt ", counter, ":")
    numb = int(input("Guess the number: "))
    if numb == 100 or numb == 200:
        print("Good guess! \n")
        if counter == 5:
            break
    else:
        if counter < 5:
            print("Try again! \n")
        else:
            break
    counter += 1

print("Game over!")