import math
from datetime import datetime


# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    
    p = 3.14

    def __init__(self, radius):
        self.radius = radius
        

    def circle_area(self):
        return self.p * self.radius ** 2

    def circle_perimeter(self):
        return 2 * self.p * self.radius
    

c = Circle(5)
print(c.circle_area())
print(c.circle_perimeter())


# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.


class Person:

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")

    def age(self):
        current_date = datetime.today()
        age = current_date.year - self.dob.year
        return age
    
p = Person("Bekzod", "Uzbekistan", "1996-12-02")
print(p.age())



# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
c = Calculator()
print('Add:', c.add(10,5))
print('Subtract:', c.subtract(10,5))
print('Multiply:', c.multiply(10,5))
print('Divide:', c.divide(10,5))


# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))



# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(self.items.values())

# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item): 
        self.stack.append(item)
    
    def pop(self): 
        return self.stack.pop() if self.stack else "Stack is empty"
    def display(self): 
        print("Stack:", self.stack)

# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): 
        self.queue.append(item)

    def dequeue(self): 
        return self.queue.pop(0) if self.queue else "Queue is empty"

# 11. Bank Class
# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name not in self.accounts:
            self.accounts[name] = Account(name)
        else:
            print("Account already exists")

    def get_account(self, name):
        return self.accounts.get(name, "Account not found")