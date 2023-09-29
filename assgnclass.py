#1. Define a class which has at least two methods one, to get a
# string from console input and other is to print the string in
# uppercase.
# class ExampleClass:
#     class_parameter = "This is a class parameter"

#     def __init__(self, instance_parameter):
#         self.instance_parameter = instance_parameter

# # Create instances of the class
# instance1 = ExampleClass("Instance 1")
# instance2 = ExampleClass("Instance 2")
# print("Class parameter:", ExampleClass.class_parameter)
# print("Instance 1 parameter:", instance1.instance_parameter)
# print("Instance 2 parameter:", instance2.instance_parameter)

#2. Define a class, which have a class parameter and have a same instance parameter.
# class MyClass:
#     # Class parameter
#     class_param = "I am a class parameter"
    
#     def __init__(self, instance_param):
#         # Instance parameter
#         self.instance_param = instance_param
# obj1 = MyClass("Instance 1")
# obj2 = MyClass("Instance 2")
# print("Class parameter:", MyClass.class_param)
# print("Instance 1 parameter:", obj1.instance_param)
# print("Instance 2 parameter:", obj2.instance_param)

#3. Define a class named Circle which can be constructed by
# radius. The Circle class has a method which can compute the
# area.
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def compute_area(self):
#         """
#         Compute the area of the circle.
#         """
#         return math.pi * self.radius**2


# circle = Circle(5)
# area = circle.compute_area()
# print(f"The area of the circle with radius {circle.radius} is {area:.2f} square units")

#4. Define a class named BankAccount. This class should contain methods withdraw() and deposit to calculate the balance amount remained in your account.
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"Deposited ${amount}. Current balance: ${self.balance}"
#         return "Invalid deposit amount. Amount must be greater than zero."

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"Withdrew ${amount}. Current balance: ${self.balance}"
#         return "Insufficient funds." if amount > 0 else "Invalid withdrawal amount."

#     def get_balance(self):
#         return f"Current balance: ${self.balance}"
# account = BankAccount(1000)
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.get_balance())


# 5.Define a class named Shape and its subclass Square. The
# Square class has an init function which takes a length as
# argument. Both classes have a area function which can print
# the area of the shape where Shape's area is 0 by default.

# class Shape:
#     def __init__(self):
#         self.area = 0

#     def calculate_area(self):
#         pass

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length

#     def calculate_area(self):
#         self.area = self.length ** 2

# # Creating instances of the Square class
# square1 = Square(5)
# square2 = Square(7)

# # Calculating and printing the areas
# square1.calculate_area()
# square2.calculate_area()

# print(f"Area of square 1: {square1.area}")
# print(f"Area of square 2: {square2.area}")

# # Creating an instance of the Shape class (default area is 0)
# shape = Shape()
# print(f"Area of a generic shape: {shape.area}")

