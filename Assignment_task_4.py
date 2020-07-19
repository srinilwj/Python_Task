#1. Write a program to reverse a string.
#Sample data: “1234abcd”
#Expected Output: “dcba4321”
def reverse_string(s):

    return s[::-1]


demo_string = "1234abcd"
result = reverse_string(demo_string)
print(result)




#2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
#Expected Output:
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

def case_calculator(x):
    demo = {}
    count_upper = 0
    count_lower = 0
    for i in range(len(x)):
        if x[i].isupper():
            count_upper += 1
            demo['upper'] = count_upper
        else:
            count_lower += 1
            demo['lower'] = count_lower
    print("No. of Upper case characters : ", demo['upper'])
    print("No. of Lower case Characters : ", demo['lower'])

user_input = str(input("Enter a string of upper and lower case characters: "))
case_calculator(user_input)





#3.        Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_function(old):
    new_list = []
    for i in old:
        if i not in new_list:
            new_list.append(i)
    return new_list


old_list = [2, 5, 2, 7, 8, "consultadd", 12, "consultadd"]
result = unique_function(old_list)
print(result)





#4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

user_input = list(input().split("-"))

def sorting(user_input):
    user_input.sort()
    return "-".join(user_input)


result = sorting(user_input)
print(result)





#5.         Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Sample input:
#Hello world
#Practice makes perfect
#Expected Output:
#HELLO WORLD
#PRACTICE MAKES PERFECT

stored = []
new_string = ""

def capitalize(stored, new_string):
    while True:
        user_input = str(input())
        if user_input == '':
            #print(stored)
            break
        else:
            stored.append(user_input)
    
    for i in stored:
        new_string = str(i.upper())
        print(new_string)
    

capitalize(stored, new_string)




#6.          Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def sum_of_two_numbers():
    first_numb = input("Enter the first number: ")
    second_numb = input("Enter the second number: ")
    result = int(first_numb) + int(second_numb)
    return result


res = sum_of_two_numbers()
print(res)




#7. Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

def max_string():
    first_string = input()
    second_string = input()
    if len(first_string) > len(second_string):
        print("The string with maximum length is: ", first_string)
    elif len(first_string) == len(second_string):
        print("Both strings have equal length: \n", first_string, "\n", second_string)
    else:
        print("The string with maximum length is: ", second_string)


max_string()





#8.        Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def squared_values():
    demo_list = []
    for value in range(2,20):
        square = value*value
        demo_list.append(square)
        demo_tuple = tuple(demo_list)
    return demo_tuple


result = squared_values()
print(result)




#9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
#Example: If the limit is 3 , it should print:
#0 EVEN
#1 ODD
#2 EVEN
#3 ODD

limit = int(input("Enter the limit: "))

def showNumbers(limit):
    for value in range(0, limit+1):
        if value%2 == 0:
            print(value, "EVEN")
        else:
            print(value, "ODD")


showNumbers(limit)






#10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

demo_list = []
for i in range(1,21):
    demo_list.append(i)

def filtering(d):
    if d%2 == 0:
        return d

result_list = list(filter(filtering, demo_list))
print(result_list)




#11. 	Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
#Hints: Use map() to generate a list.
#     	     Use filter() to filter elements of a list
#            Use lambda to define anonymous functions


demo = list(map(int, range(1,11)))

def even_number(n):
        if n%2 == 0:
            return n
    
filter_list = list(filter(lambda x:(x%2==0), demo))

print("The list of even numbers : ",filter_list)
#squared = lambda x: x*x
print("The squared list: ", list(map(lambda n:n*n, filter_list)))





#12. 	Write a function to compute 5/0 and use try/except to catch the exceptions

try:
    def compute():
        res = 5/0
        return res



    result = compute()
    print(result)

except ZeroDivisionError:
    print("The number in the denominator is zero, which is why it cannot be calculated....Sorry!")





#13. 	Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
#Goal : Turn [1,2,3,4,5,6,7] to 1234567 
from functools import reduce

demo = [[1,2,3],[4,5],[6,7,8]]

result = (reduce((lambda x,y: x + y), demo))
print(result)





# 14. (i) 

def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

'''
This program prints 2 which is in the finally block
'''
# (ii) 
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()

'''
This program gives an error because in the try block, there is a function called 'f(x,4)' where no such function name is defined anywhere...
Furthermore, it prints 'after f', which is in the finally block, because the finally block runs irrespective of the try block whether it is true or false
'''