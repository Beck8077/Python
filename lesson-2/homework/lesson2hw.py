# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

user_name = input('Write your name: ')
user_age = int(input('Write your year of birth: '))
print(f'Hi {user_name}, you are {2025 - user_age} years old.')

# 2. Extract Car Names
# Extract car names from the following text:

txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])

# 3. Extract Car Names
# Extract car names from the following text:

txt = 'MsaatmiazD'
print(txt[::2])
print(txt[-1::-2])

# 4. Extract Residence Area
# Extract the residence area from the following text:

txt = "I'am John. I am from London"
print(txt[21:])

# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.

user_input = input('Write your word: ')
reverse_user_input = user_input[::-1]
print(reverse_user_input)


# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.

word = list(input('Write your word: ').strip(' '))
vowels = 'aeuioAEUIO'
counter = 0
for w in word:
    if w in list(vowels.strip(' ')):
        counter += 1

print(counter)


# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = input('Write the list of numbers: ').strip('')
numbers_splitted = list(numbers.split(' '))
maximum = 0

for number in numbers_splitted:
    if int(number) > maximum:
        maximum = int(number)

print(maximum)

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input('Write your word: ')

if word.lower() == word[::-1]:
    print(f'Yes, {word} is a palindrome')
else:
    print(f'No, {word} is not palindrome')


# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.



# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.

import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '123456789'
special_char = '@#$%^&*'

password = random.sample(alphabet + alphabet.upper() + numbers + special_char, k = 10)
print(''.join(password))