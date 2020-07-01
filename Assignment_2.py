'''
1.	Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “c” as a string
If a number is divisible by both 3 and 5 its should print “Consultadd Python Training” as a string.
'''

x = eval(input("Enter a number: "))

if x%3==0 and x%5==0:
    print("Consultadd Python Training")
elif x%3==0:
    print("Consultadd")
elif x%5==0:
    print("c")



'''
2. 	Write a program in Python to perform the following operator based task:
Ask the user to choose the following option first:
If User Enter 1 - Addition 
If User Enter 2 - Subtraction
If User Enter 3 - Division
If USer Enter 4 - Multiplication
If User Enter 5 - Average
Ask the user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
Ask the user to enter two more numbers as first1 and second2 for calculating the average as soon as the user chooses an option 5.
In the end, if the answer of any operation is Negative print a statement saying “Zsa”
NOTE: At a time users can perform one action at a time.
'''

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



'''
3. 	Write a program in Python to implement the given flowchart:
'''

age = 38

if age >= 11:
    print("You are eligible to see the Football match.")
    if age <= 20 or age >= 60:
        print("Ticket price is $12")
    else:
        print("Ticket price is $20")
else:
    print("You are not eligible to but a ticket.")



'''
4.  Write a program in Python to break and continue if the following cases occur:
If a user enters a negative number just break the loop and print “It’s Over”
If a user enters a positive number just continue in the loop and print “Good Going”
'''

number = int(input("Enter a number: "))

while(number >= 0):
    print("Good Going")
    number = int(input("Enter a number again: "))
print("Its over")



'''
5.   Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.
'''

for i in range (2000,3201):
    if i%7 == 0 and not i%5 == 0:
        print (i)


'''
6. What is the output of the following code examples?
x=123 
for i in x:
	print(i)

OUTPUT: if x is an integer ‘123’, the for loop will show error as there is not iteration to it

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(“error”)

OUTPUT: 0 
        error 
        1 
        error 
        2


count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break

OUTPUT: 0
        1
        2
        3
        4
'''  



'''
7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
    
   Expected output: 0 1 2 4 5
Note: Use the ‘continue’ statement
'''

for number in range(0, 7):
    if number == 3 or number == 6:
        continue
    print(number)



'''
8.  Write a program that accepts a string as an input from the user and calculates the number of digits and letters.
     Expected output: consul12
     Letters 6
     Digits 2
'''

user_input = input('Enter a string: ')
char_total = 0
digit_total = 0

for c in user_input:
    if c.isalpha():
        char_total += 1
    elif c.isdigit():
        digit_total += 1
print("Letters: ", char_total)
print("Digits: ", digit_total)



'''
9. Read the two parts of the question below: 
 Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 
Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question of whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
'''

#PART 1, Lucky number is 7
user_guess = int(input("Guess the lucky number: "))

while True:
    if user_guess == 7:
        print("Congratulations! You've nailed it! :)")
        break
    else:
        print("Oops sorry,  no luck this time \n")


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



'''
10.  Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
           		counter=1
		While counter <= 5:
			print(“Type in the”, counter, “number”
			counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess, it stops and prints “Game over!”.
'''


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



'''
11.  In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.
'''


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