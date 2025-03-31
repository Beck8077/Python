# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.

fruit_list = ['apple', 'orange', 'peach', 'grape', 'banana']
print(fruit_list[2])

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.

nums1 = list(range(1,11))
nums2 = list(range(5,16))
nums3 = nums1 + nums2
print(nums3)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

nums = list(range(1, 18, 2))
new_nums = []

pop1 = nums.pop(0)
pop2 = nums.pop(len(nums)//2)
pop3 = nums.pop(-1)
print(nums)

new_nums.append(pop1)
new_nums.append(pop2)
new_nums.append(pop3)
print(new_nums)


# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.

fav_movies = ['Interstellar', 'Star Wars', 'Lord of the rings', 'Schindler"s List', 'Fight Club']
fav_movies_tuple = tuple(fav_movies)
print(fav_movies_tuple)

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.

cities = ['Tashkent', 'London', 'Paris', 'New York', 'Moscow']
for city in cities:
    if city == 'Paris':
        print(city, cities.index(city))


# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

nums = list(range(1,20,3))
copy_nums = nums.copy()
print(copy_nums)

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.

nums = list(range(10, 30, 4))
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

nums = tuple(range(1, 11))
print(nums[3:7])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.

colors = ['blue', 'red', 'blue', 'green', 'black', 'blue']
print(colors.count('blue'))


# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

animals = ('Monkey', 'Lion', 'Tiger', 'Cat', 'dog')
print(animals.index('Lion'))

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

nums1 = tuple(range(4, 25, 3))
nums2 = tuple(range(25, 50, 4))
nums3 = nums1 + nums2
print(nums3)

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.

nums_list = list(range(1, 20))
nums_tuple = tuple(range(1, 20, 2))
print(len(nums_list))
print(len(nums_tuple))

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.

tuple_nums = tuple(range(1,10))
list_nums = list(tuple_nums)
print(list_nums)

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

nums_tuple = tuple(range(7, 30))
print(f'Minimum value is: {min(nums_tuple)}. Maximum: {max(nums_tuple)}')

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.

words = ('Word', 'Phone', 'Headphones', 'Tablet', 'Cup', 'Monitor')
reversed_words = words[::-1]
print(reversed_words)