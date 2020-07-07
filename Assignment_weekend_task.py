#1.	Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.
random_list = [10, "Srinil", 1+5j, 30.45, 11, "Walanj", 2, 88.09, 3j-2, "Consultadd"]
print(random_list)


#2. 	Create a list of size 5 and execute the slicing structure 
random = [50, 60, 20, 80, 40]
print(len(random))
print(random[2:5])
print(random[:5])
print(random[2:])
print(random[:])
print(random[2:5:2])



#3. 	Create a list of given structure and run 
#	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

#Access list [1, 2, 3, 4]
print("\nFirst output: ", x[5][:4])

#Access list [600, 700]
print("\nSecond output: ", x[6:8])

#Access list [100, 300, 500, 600, 800]
print("\nThird output: ", x[::2])

#Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
new_list = []
new_list = [x[::-1]]
print("\nFourth output: ", new_list)

#Access list [10]
print("\nFifth output: ", [x[5][5][0]])

#Access list [ ]
print("\nSixth output: ", x)




#4. 	Create a list of thousand numbers using range and xrange and see the difference between each other.

x = list(range(1, 1001))
print "The range function output is", x
y = xrange(1, 1001)
z = list(y)
print "The range function output is", z 



#5. 	How Tuple is beneficial as compared to the list?

#List is mutable whereas a tuple is immutable. 
#Immutable data structres come into place where there are some fields required unchanged. 
#A list is not a perfect fit for that condition.
#So a tuple is used in such scenarios where the data stored should not be changed.



#6. 	Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.

numb = list(range(1,101))
print(numb)
new_list = []
for i in numb:
    if i%3 == 0 and i%2 == 0:
        new_list.append(i)

print(new_list)



#7. 	Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.

letter = "I am learning python with consultadd"
new_string = letter[::-1]
print(letter)
print("\n")
print(new_string)
print("\n")
demo = {}

for i in range(len(new_string)):
    if new_string[i] == 'a' or new_string[i] == 'e' or new_string[i] == 'i' or new_string[i] == 'o' or new_string[i] == 'u':
        demo[i] = new_string[i]

print(demo)



#8. 	Write a program in Python to iterate through the string “hello my name is Abcde” and print the string which has even length of the word.

given_string = "hello my name is Abcde"
result_string = []
for i in range(len(given_string)):
    if i%2 == 0:
        result_string.append(given_string[i])

print(result_string)



#9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
result_num = 8
pairs = []
for i in range(len(x)):
    for j in range(len(x)):
        if x[i] == x[j]:
            continue
        elif x[i] + x[j] == 8:
            if x[i] in pairs or x[j] in pairs:
                continue
            else:
                pairs = [x[i], x[j]]
            print(pairs)



#10. 	Write a program in Python to complete the following task:
#Create two different lists as in even_list and odd_list
#Ask the user to enter the number in the range of 1,50 and make sure if the entered number is even appended it to the even_list and if the entered number is odd append it to the odd list.
#Keep that in mind you can only add 5 items in each list
#Make sure once you entered the total 5 elements calculate the sum of the list and return the maximum out of the list.

even_list = list()
odd_list = list()
while True:
    print("\n")
    user_entry = int(input("Enter any number between 1-50: "))
    if len(even_list) > 4 and len(odd_list) > 4:
        print("\nBoth even and odd lists have 5 values")
        print("\nThe sum of even list is ", sum(even_list))
        print("\nThe maximum number from even list is ", max(even_list))
        print("\nThe sum of odd list is ", sum(odd_list))
        print("\nThe maximum number from odd list is ", max(odd_list))
        break
    elif user_entry%2 == 0:
        if len(even_list) > 4:
            print("\nMaximum of 5 elements can be appended in the even list")            
            continue
        else:
            even_list.append(user_entry)
            print("\nNumber added to the even list")
    else:
        if len(odd_list) > 4:
            print("\nMaximum of 5 elements can be appended in the odd list")            
            continue
        else:
            odd_list.append(user_entry)
            print("\nNumber added to the odd list")

print("\nThe even list is ", even_list)
print("\n")
print("\nThe odd list is ", odd_list)



#11. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement. 
# Example: 12abcbacbaba344ab  
#                      Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic
input_string = "12abcbacbaba344ab"
print(type(input_string))

demo = dict()
for i in input_string:
    if i in demo:
        demo[i] += 1
    elif i.isdigit():
        continue
    else:
        demo[i] = 1

print(demo)



#12.          Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
given_tuple = (1,2,3,4,5,6,7,8,9,10)
demo_list = list()
for i in given_tuple:
    if i%2 == 0:
        demo_list.append(i)

result_tuple = tuple(demo_list)
print(result_tuple)
print(type(result_tuple))