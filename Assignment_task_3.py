#1.	Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.
random = [10, "Srinil", 1+5j, 30.45, 11, "Walanj", 2, 88.09, 3j-2, "Consultadd"]
print(random)


#2. 	Create a list of size 5 and execute the slicing structure 
random = [50, 60, 20, 80, 40]
print(len(random))
print(random[2:5])
print(random[:5])
print(random[2:])
print(random[:])
print(random[2:5:2])


#3.          Write a program to get the sum and multiply of all the items in a given list.
random_list = [10, 20, 80, 30, 25]
res1 = sum(random_list)
print(res1)

#Using for loop

product = 1
for element in random_list:
    product = product * element

print(product)

#Using while loop

i = 0
mult = 1
while True:
    if random_list[i] == random_list[-1]:
        mult = mult * random_list[i]
        break
    else:
        mult = mult * random_list[i]
        i += 1

print(mult)



#4.   	Find the largest and smallest number from a given list.
given_list = [3, 8, 1, 10, 7]

print(min(given_list))
print(max(given_list))



#5. 	Create a new list that contains the specified numbers after removing the even numbers from a predefined list.
predefined_list = [12,13,24,85,36,97]
new_list = []

for i in predefined_list:
    if i%2 == 0:
        pass
    else:
        new_list.append(i)

print(new_list)




#6.	Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
squared_list = []

for first_5 in range(1,6):
    square_1 = first_5 * first_5
    squared_list.append(square_1)


for last_5 in range(26,31):
    square_2 = last_5 * last_5
    squared_list.append(square_2)

print(squared_list)



#7.	Write a program to replace the last element in a list with another list.
#Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
#Expected output: [1,3,5,7,9,2,4,6,8]

sample_data = [[1,3,5,7,9,10],[2,4,6,8]]
first_half = sample_data[0]
second_half = sample_data[1]
first_half.pop()
final_list = first_half + second_half

print(final_list)




#8.	Create a new dictionary by concatenating the following two dictionaries:
#a={1:10,2:20}
#b={3:30,4:40}
#Expected Result: {1:10,2:20,3:30,4:40}

a = {1:10, 2:20}
b = {3:30, 4:40}
a.update(b)
print(a)

#Another way of concatenating dictionary
a = {1:10, 2:20}
b = {3:30, 4:40}
c = {**a, **b}
print(c)



#9.	Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#Sample data (n=5)
#Expected Output: {1:1,2:4,3:9,4:16,5:25}

n = 10
square_dict = {}
for i in range(1,n+1):
    square_dict[i] = i*i

print(square_dict)



#10. 	Write a program which accepts a sequence of comma-separated numbers from the console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#The output should be:
#[‘34’,’67’,’55’,’33’,’12’,’98’]
#(‘34’,’67’,’55’,’33’,’12’,’98’)

seq_generate = eval(input("Enter a sequence of numbers: "))

a_list = []
a_list.extend(seq_generate)
print(a_list)

a_tuple = (seq_generate)
print(a_tuple)