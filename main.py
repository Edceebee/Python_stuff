# 2.1 (What does this code do?) Create the variables x = 2 and y = 3, then determine what
# each of the following statements displays:
# a) print('x =', x)
# b) print('Value of', x, '+', x, 'is', (x + x))
# c) print('x =')
# d) print((x + y), '=', (y + x))
#
# x = 2
# y = 3
# print('x =', x)
# print('value of', x, '+', x, 'is', (x + x))
# print('x =')
# print((x + y), '=', (y + x))
#
# 2.2 (What’s wrong with this code?) The following code should read an integer into the
# variable rating:
#
# rating = input('Enter an integer rating between 1 and 10')
#
# (Fill in the missing code) Replace *** in the following code with a statement that
# will print a message like 'Congratulations! Your grade of 91 earns you an A in this
# course'. Your statement should print the value stored in the variable grade:
# if grade >= 90:
#     ***
#
# grade=int(input("enter your grade"))
# if grade >= 90:
#  print('Congratulations! Your grade of 91 earns you an A in this course')
#
#
# (Arithmetic) For each of the arithmetic operators +, -, *, /, // and **, display the
# value of an expression with 27.5 as the left operand and 2 as the right operand.
# 27.5 + 2
# 27.5 - 2
# 27.5 * 2
# 27.5 / 2
# 27.5 // 2
# 27.5 ** 2
#
#
# (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter,
# circumference and area. Use the value 3.14159 for π. Use the following formulas
# (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
# introduce Python’s math module which contains a higher-precision representation of π.]
# pie = 3.14159
#
# radius = int(input("Enter radius : "))
#
# area = pie * radius* 2
# diameter = 2 * radius
# circumference = 2 * pie * radius
#
# print("Area is " "= ", area)
# print("Diameter is " "= ", diameter)
# print("Circumference is " "= ", circumference)
#
#
# (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
# leaves a remainder of 0 when divided by 2.]
#
# number = int(input("Enter number : "))
# if number % 2 == 0:
#     print("The number entered is an even number")
# else:
#     print("The number entered is an odd number")
#
# (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and
# whether 2 is a multiple of 10. (Hint: Use the remainder operator.)
#
# number1 = int(input("Enter first number :"))
# number2 = int(input("Enter second number :"))
#
# if number2 % number1 == 0:
#     print(number2, "is a multiple of", number1)
#
# else:
#     print(number2, "is not a multiple of", number1)
#
#
# (Table of Squares and Cubes) Write a script that calculates the squares and cubes
# of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
# the tab escape sequence to achieve the three-column output.
# number square cube
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125
#
# print("numbers   squares   cube\n0         0         0\n1         1         1\n2         4         8\n3
# 9     "      "    27\n4         16 "      "       64\n5         25        125")
#
#
# my_list = {1, 2, 3, 4, 5}  # creating a list
# print(my_list)
#
# my_list.append(6)   # appending a number
# print(my_list)
#
# my_list.insert(0, 99)  # inserting a new number in the list
# print(my_list)
#
# my_list[0] += 1   # adding 1 to the value of the first index
# print(my_list)
#
# my_list += [15]   # using concatenation to include a value which is similar to extend
# print(my_list)
#
# my_list.remove(100)  # removing a  specified value
# print(my_list)
#
# my_list.pop()      # removing the last number in the list
# print(my_list)
#
# my_new_list = ['john', 'charles', 'dawn', 'pater']
# print(my_new_list)
#
# my_new_list = "-".join(my_new_list)   # joining with "-"
# print(my_new_list)
#
# first_int = 10
# second_int = 20
# if first_int > second_int:
#     print("the first int is bigger")
# else:
#     print("the second int is bigger")
# new_set = {1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5}
# print(new_set)
#
#  defining function
# def multiply(num1: float, num2: float) -> float:
#     num3 = num1 * num2
#     return num3
