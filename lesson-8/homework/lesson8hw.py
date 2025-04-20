# Exception Handling Exercises
# 1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    zero_div = 10 / 0
except ZeroDivisionError:
    print('You can"t divide by zero')


# 2 Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

number = input('Write down a number: ')

try: 
    num = int(number)
    print(num ** 2)
except ValueError:
    print('You can only write numbers not letters')


# 3 Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try: 
    with open('new_stuff.txt') as f:
        f.read()
        print(f)
except FileNotFoundError:
    print('There is no such a file!')

# 4 Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.




# 5 Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    with open("f19_practice.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("You do not have permission to access this file.")

# 6 Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index is out of range!")

# 7 Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    num = input("Enter a number (Ctrl+C to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

# 8 Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    a = 1.0
    b = 0.0
    result = a / b
except ArithmeticError as e:
    print("Arithmetic error occurred:", e)

# 9 Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    filename = input("Enter the filename: ")
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
except UnicodeDecodeError:
    print("UnicodeDecodeError: Unable to decode file with UTF-8 encoding.")

# 10 Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    my_list = [1, 2, 3]
    my_list.appendd(4) 
except AttributeError:
    print("Attribute does not exist for the list.")


# ==================================================================


# 1 Write a Python program to read an entire text file.

with open('lesson8/f19_practice.txt') as f:
    s = f.read()
    print(s)

# 2 Write a Python program to read first n lines of a file.

with open('lesson8/f19_practice.txt') as f:
    s = f.readline()
    print(s)

# 3 Write a Python program to append text to a file and display the text.

with open('lesson8/f19_practice.txt', 'a') as f:
    s = f.write('Maab Academy')

with open('lesson8/f19_practice.txt') as f:
    s = f.read()
    print(s)

