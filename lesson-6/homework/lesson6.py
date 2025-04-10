# 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it,
#  shift the underscore placement to the next character. No underscore should be added at the end.

# Examples
# Input: hello Output: hel_lo

# Input: assalom Output: ass_alom

# Input: abcabcabcdeabcdefabcdefg Output: abc_abc_abcd_abcd_abcdef




# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.


n = int(input('Write your number: '))
for i in range(1, n):
    sqr_nums = i**2

    print(sqr_nums)


# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop

n = 0
while True:
    if n == 10:
        break

    n += 1
    print(n)

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = int(input('How many rows there: '))

for r in range(rows):
    for o in range(r):
        print(o + 1, end=' ')
    
    print()


# Exercise 3: Calculate sum of all numbers from 1 to a given number

num = int(input('Write your number: '))
summ = 0
for r in range(1, num + 1):
    summ += r

print(summ) 


# Exercise 4: Print multiplication table of a given number

num = int(input('Write a number: '))

for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

# Exercise 5: Display numbers from a list using a loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected Output:

# 75
# 150
# 145



# Exercise 6: Count the total number of digits in a number

num = int(input('Write your number: '))
cnt = 0

while num != 0:
    num //= 10
    cnt += 1

print(cnt)


# Exercise 7: Print reverse number pattern

rows = int(input('How many rows there: '))

for r in range(rows, 0, -1):
    for o in range(r):
        print(r - o, end=' ')
    
    print()

# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

for l in range(len(list1) // 2):
    list1[l], list1[-1 - l] = list1[-1 - l],  list1[l]

print(list1)


# Exercise 9: Display numbers from -10 to -1 using a for loop

num = -10

for i in range(-10, 0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution

num = 0

while num <= 4:
    print(num)
    
    if num == 4:
        print('Done!')

    num += 1


# Exercise 11: Print all prime numbers within a range

def is_prime(n: int):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False 

    return True 

def prime_numbers(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

prime_numbers(25, 50)

# Exercise 12: Display Fibonacci series up to 10 terms

def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        c = a
        a = b
        b = c + b

    return result

print(fibonacci(10))    

# Exercise 13: Find the factorial of a given number

def custom_fact(number):
    if number in [0, 1]:
        return number
    else:
        return number * custom_fact(number - 1)
print(custom_fact(5))

# 4. Return Uncommon Elements of Lists

list1 = [1,1,2]
list2 = [2,3,4]
list3 = list(set(list1) ^ set(list2))
print(list3)

