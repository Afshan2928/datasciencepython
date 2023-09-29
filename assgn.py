# 1. Write a Python program to print the following string in a specific format .Sample String : &quot;Twinkle, twinkle, little star, How I wonder what you are! Up above
# the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I
# wonder what you are&quot;
# Output :
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# Twinkle, twinkle, little star,
# How I wonder what you are
#ans)
# string1="Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# lines=string1.split(", ")
# print(lines)
# for i,line in enumerate(lines):
#     print(f"{line}")

#2. Write a Python program to find out what version of Python you are using.
# import sys
# print("python version:")
# print(sys.version)
# print("version_info")
# print(sys.version_info)

# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14
# ans)
# import datetime
# current_datetime=datetime.datetime.now()
# formatted_datetime=current_datetime.strftime("%Y-%m-%D %H-%M-%S")
# print("current date and time")
# print(formatted_datetime)

#4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# import math
# radius_str=input("enter the given radius")
# radius=float(radius_str)
# area=math.pi*(radius**2)
# print(f"area of the given circle is:{area}")

# 5. Write a Python program to display the first and last colors from the following list.
# color_list = [Red,Green,White,Black]
# color_list=["red","green","white","black"]
# print(color_list[0])
# print(f"first color of the list is {color_list[0]}")
# print(color_list[2])
# print(f"last colour of the list is:{color_list[2]}")

#6.Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# def different_sequences(numbers):
#     unique_numbers=set(numbers)
#     if len(unique_numbers)==len(numbers):
#         return True
#     else:
#         return False
# sequences1=[1,2,3,4,5,6,7]
# sequences2=[1,2,3,6,7,9,4,4]
# print("sequences1",different_sequences(sequences1))
# print("sequences2",different_sequences(sequences2))

#8.Write a Python program that removes and prints every third number from a list of numbers until the list is empty.
# numbers=[1,2,3,4,5,6,7,8,9]
# count=0
# while numbers:
#     count+=1
#     if count%3==0:
#         removed_numbers=numbers.pop(0)
#         print("removed:",removed_numbers)
#     else:
#         numbers.append(numbers.pop(0))

#7. Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and'I'. Ensure that each character is used only once.
# from itertools import permutations
# characters=["a","e","i","o","u"]
# perms=permutations(characters)
# for perm in perms:
#     perm_string=" ".join(perm)
#     print(perm_string)

#9.Write a Python program to identify unique triplets whose three elements sum to zero from an array of n integers.
# from itertools import combinations
# arr=[-1,0,1,2,-1,-4]#-1+0+1 first triplet should be zero
# triplets=set()
# for triplet in combinations(arr,3):
#     if sum(triplet)==0:
#         triplets.add(tuple(sorted(triplet)))
# for triplet in triplets:
#     print(triplet)

#10.Write a Python program to make combinations of 3 digits.
# from itertools import combinations
# digits=[0,1,2,3,4,5,6,7,8,9]
# combinations_list=list(combinations(digits,3))
# for comb in combinations_list:
#     print(comb)

#11. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def calculate_circle_area(self):
#         return math.pi*self.radius**2
#     def calculate_circle_perimeter(self):
#         return 2*math.pi*self.radius
# radius=float(input("enter given intergers"))
# circle=Circle(radius)
# area=circle.calculate_circle_area()
# perimeter=circle.calculate_circle_perimeter()
# print("area of the circle",area)
# print("perimetr of the circle",perimeter) 

# 12.Write a Python program to create a person class. Include attributes like name, country
#  and date of birth. Implement a method to determine the person's age.
# from datetime import date
# class Person:
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=date_of_birth
#     def calculate_age(self):
#         today=date.today()
#         age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    
#         return age
# person1=Person("Meera","India",date(1982,7,21))
# person2=Person("maya","indonasia",date(1983,8,24))
# person3=Person("Anaya","Malayasia",date(1991,2,18))

# print("Person 1:")
# print("Name:", person1.name)
# print("Country:", person1.country)
# print("Date of Birth:", person1.date_of_birth)
# print("Age:", person1.calculate_age())

# #method 2
# from datetime import date
# class Person:
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age

# # Example usage
# person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
# person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
# person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))
# # Accessing attributes and calculating age
# print("Person 1:")
# print("Name:", person1.name)
# print("Country:", person1.country)
# print("Date of Birth:", person1.date_of_birth)
# print("Age:", person1.calculate_age())

# print("\nPerson 2:")
# print("Name:", person2.name)
# print("Country:", person2.country)
# print("Date of Birth:", person2.date_of_birth)
# print("Age:", person2.calculate_age())

# print("\nPerson 3:")
# print("Name:", person3.name)
# print("Country:", person3.country)
# print("Date of Birth:", person3.date_of_birth)
# print("Age:", person3.calculate_age())

# 13. Write a Python program to create a calculator class. Include methods for basic arithmetic
# operations.
# class Calculator:
#     def add(self,num1,num2):
#         return num1+num2
#     def substract(self,num1,num2):
#         return num1-num2
#     def multiply(self,num1,num2):
#         return num1*num2
#     def divide(self,num1,num2):
#         if num2==0:
#             print("cannot be divide bu zero")
#         return num1/num2
# calculator=Calculator()
# num1=float(input("enter an interger"))
# num2=float(input("enter an interger"))
# print(f"{num1}+{num2}={calculator.add(num1,num2)}")
# print(f"{num1}-{num2}={calculator.substract(num1,num2)}")
# print(f"{num1}*{num2}={calculator.multiply(num1,num2)}")
# print(f"{num1}/{num2}={calculator.divide(num1,num2)}")

# 14. Write a Python program to create a class that represents a shape. Include methods to
# calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle,
# and square.
# import math
# class Shapes:
#     def area(self):
#         pass
#     def perimeter(self):
#         pass
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*self.radius**2
#     def perimeter(self):
#         return 2*math.pi*self.radius
# class Triangle:
#     def __init__(self,side1,side2,side3):
#         self.side1=side1
#         self.side2=side2
#         self.side3=side3
#     def area(self):
#         s=(self.side1+self.side2+self.side3)/2
#         return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
#     def perimeter(self):
#         return self.side1+self.side2+self.side3
# class Square:
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side**2
#     def perimeter(self):
#         return 4*self.side
# circle=Circle(4)
# triangle=Triangle(2,3,4)
# square=Square(6)
# print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")
# print(f"Triangle - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")
# print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}")

#15. Write a Python program to create a class representing a bank. Include methods for
# managing customer accounts and transactions.
# def are_all_numbers_different(numbers):
#     """
#     Check if all numbers in the given sequence are different from each other.
#     """
#     seen = set()  # Create an empty set to store seen numbers

#     for num in numbers:
#         if num in seen:
#             return False  # If the number is already in the set, it's not unique
#         seen.add(num)  # Add the number to the set

#     return True  # All numbers in the sequence are unique

# # Example usage
# sequence1 = [1, 2, 3, 4, 5]
# sequence2 = [1, 2, 3, 4, 2]

# print(are_all_numbers_different(sequence1))  # True
# print(are_all_numbers_different(sequence2))  # False


# 17. Write a Python program to create a tuple of numbers and print one item.
# Create a tuple of numbers
# my_tuple = (1, 2, 3, 4, 5)

# Print one item from the tuple (e.g., the item at index 2, which is the third item)
# item_to_print = my_tuple[2]
# print("Item at index 2:", item_to_print)

# 19. Write a Python program to get the smallest number from a list.
# numbers=[5,2,6,7,1]
# smallest_numbers=min(numbers)
# print("the smallest numbers is",smallest_numbers)

