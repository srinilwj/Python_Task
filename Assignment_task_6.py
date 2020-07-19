#1.	Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError

while True:
    try:
        x = in(input("Please enter a number: "))
        break
    except SyntaxError:
        print("Oops!  That was no valid number.  Try again...")





#2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.

from sys import argv

program_name, file_name = argv

#print(program_name)
#print(file_name)

while True:
    try: 
        file_handler = open(file_name, 'r')
        reader = file_handler.read()
        print(reader)
        break
    except:
        print("Unfortunately, the given file name is not correct, please enter the name again...")
        file_name = input("Enter the file name here: ")





#3. 	Write a program to handle an error if the user entered the number more than four digits it should return “Please length is too short/long !!! Please provide only four digits” 

value = input("Enter the numbers here: ")
while True:
    try:
        if len(value) < 5:
            print(value)
            break
        else:
            raise Exception
    except:
        print("Please length is too short/long !!! Please provide only four digits")
        value = input("Enter again: ")





#4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

uname = input("Username: ")
pword = input("Password: ")
pword_2 = input("Re-Type Password: ")
record = {'username' : 'Srinil', 'password' : 'abcde'}
count = 0
decrementor = 4
while True:
    try:
        if uname == record['username']:
            if pword == record['password']:
                if pword_2 == record['password']:
                    print("Successfully logged in :)")
                    break
                else:
                    raise Exception
            else:
                raise Exception
        else:
            print("Username is not valid, please enter your information again")
            uname = input("Username: ")
            pword = input("Password: ")
            pword_2 = input("Re-Type Password: ")
    except:
        count += 1
        decrementor -= 1
        if count < 4:
            if decrementor == 1:
                print(f"Please, type the password again carefully, you just have {decrementor} more attempt")
                pword = input("Password: ")
                pword_2 = input("Re-Type Password: ")
            else:
                print(f"Please, type the password again, you have {decrementor} more attempts")
                pword = input("Password: ")
                pword_2 = input("Re-Type Password: ")
        else:
            print("Sorry, maximum attempts reached, better luck next time!!")
            break