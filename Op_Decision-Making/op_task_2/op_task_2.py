choice = int(input("Choose an option from the following - 1 (Addition), 2 (Subtraction), 3 (Division), 4 (Multiplication) or 5 (Average): "))

if choice <= 5 and choice >= 1:
    first_variable = int(input("Enter the first value: "))
    second_variable = int(input("Enter the second value: "))
    if choice == 1:
        result = first_variable + second_variable
        if result < 0:
            print("Zsa")
        else:
            print(result)
    elif choice == 2:
        if second_variable > first_variable:
            print("Zsa")
        else:
            result = first_variable - second_variable
            print(result)
    elif choice == 3:
        result = first_variable / second_variable
        if result < 0:
            print("Zsa")
        else:
            print(result)
    elif choice == 4:
        result = first_variable * second_variable
        if result < 0:
            print("Zsa")
        else:
            print(result)
    elif choice == 5:
        first1 = int(input("Enter third value: "))
        second2 = int(input("Enter fourth value: "))
        result = (first1 + second2 + first_variable + second_variable) / 4
        if result < 0:
            print("Zsa")
        else:
            print(result)
else:
    print("Invalid option!!")