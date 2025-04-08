# 1. 
def is_leap(year): 
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else: 
        return False
    
leap_or_no = int(input('Write down a year: '))    
print(is_leap(leap_or_no))


# 2. Conditional Statements Exercise

n = int(input('Write down an integer: '))

if n % 2 != 0:
    print('Weird')
elif (n % 2 == 0) and (2 <= n <= 5):
    print('Not Weird')
elif (n % 2 == 0) and (6 <= n <= 20):
    print('Weird')
elif (n % 2 == 0) and (n > 20):
    print('Not Weird')


# 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.

# Solution 1 with if-else statement.

def new_list(a, b):
    if a > b:
        return []
    if a % 2 != 0:
        a += 1
    if b % 2 != 0:
        b -= 1
    if a > b:
        return []
    return list(range(a, b + 1, 2))


# Solution 2 without if-else statement.

a = int(input('Write your first number: '))
b = int(input('Write your second number: '))


l = list(filter(lambda x:x%2==0, range(a, b+1)))
print(l)