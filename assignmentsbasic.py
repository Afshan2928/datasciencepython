#1.Write aprogram to check whether entered number is positive or negative.
# num=int(input("enter number"))
# if(num>0):
#     print("number is positive")
# else:
#     print("number is negative")

#2.Write a program to swap variables
# x=int(input("enter varible of x"))
# y=int(input("enter variable of y"))
# z=x
# x=y
# y=z
# print("after swapping:")
# print("x=",x)
# print("y=",y)


#3.Write a program to determine if year is leap or not
# year=int(input("enter given year"))
# if(year%4==0 and year%100!=0)or(year%400==0):
#     print("year is leap year")
# else:
#     print("year is not leap year")

#4.Write a program to check whether the given number is odd or even
# num=int(input("enter a number"))
# if(num%2==0):
#     print("the number is even")
# else:
#     print("number is odd")

#write a program to print fibonacci series
# Get the number of terms for the Fibonacci series from the user

# n = int(input("Enter the number of terms in the Fibonacci series: "))

# # Initialize the first two terms
# a, b = 0, 1

# # Check if the number of terms is valid
# if n <= 0:
#      print("Please enter a positive integer.")
# elif n == 1:
#      print("Fibonacci Series:")
#      print(a)
# else:
#      # Print the first two terms
#      print("Fibonacci Series:")
#      print(a, b, end=" ")

#      # Generate and print the remaining terms
#      for _ in range(2, n):
#          next_term = a + b
#          print(next_term, end=" ")
#          a, b = b, next_term

# print()  # Print a newline for better formatting

#6.Write a program to generate following pyramid or traingle like given below using for loop
#a)******
#  *****
#  ****
#  ***
#  **
#  *
# n=6
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print() 

#b)
# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range (n):
#     for j in range(n-i-1):
#         print("*",end="")
#     print()

#7) write a prgm to print prime numbers between given interval
# lower=500
# upper=1000
# print("prime numbers between",lower,"and",upper,"are")
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if(num%i)==0:
#                 break
#         else:
#             print(num)
#8) write a prgm to print odd numbers between 1 and 50 and calculate sum of that numbers
# sum=0
# for i in range(1,51):
#     if(i%2)!=0:
#         print(i)
#         sum+=i
# print("sum of odd numbers",sum)

#9)Write a prgm to find factorial of the given number
# n=int(input("enter factorial number"))
# factorial=1
# if(n<0):
#     print("factorial cannot be -ve")
# elif(n==0):
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,n+1):
#         factorial*=i
#         print("factorial of a number",factorial)


#10)Write a prgm to check whether the string is pallindrome or not
# x="malayalam"
# y=""
# for i in x:
#     y=i+y
# if(x==y):
#     print("yes")
# else:
#     print("no")

#11)Write pgrm to fins sum of all integers greater than 100 and less than 200 that are divisible by 7
# lower=int(input("enter a number"))
# upper=int(input("enter a number"))
# for i in range(lower,upper+1):
#     if(i%7==0):
#         print(i)

#12) write a program to display multiplication table
# num=int(input("enter a number"))
# print("table of: ")
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

#13) write pgm to calculate are and perimeter of rectangle
# lenght=float(input("enter length"))
# breadth=float(input("enter breadth"))
# area=lenght*breadth
# perimeter=2*(lenght+breadth)
# print("area",area)
# print("perimeter",perimeter)

#14) write a pgm to find sum of n natural numbers
# num=int(input("enter a natural number"))
# if(num<0):
#     print("not a natural number")
# else:
#     sum=0
#     while(num>0):
#         sum+=num
#         num-=1
#     print("sum of natural numbers is",sum)

#15)to check if the no is an amstrong no or not
# num=int(input("enter a number"))
# sum=0
# #find the sum of cube of each digit
# temp=num
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# #to display result
# if num==sum:
#     print(num,"is amstrong no")
# else:
#     print(num,"not")

#write a prm patter prnting
# 1
# 2 3
# 4 5 6
# 7 8 9
# n=4
# current_num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(current_num,end="")
#         current_num+=1
#     print()

#16 .write pgm to find largest among 3 numbers
# Input three numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# # Find the largest number using the max() function
# largest = max(num1, num2, num3)

# # Display the result
# print(f"The largest number among {num1}, {num2}, and {num3} is {largest}")

# 18.write a pgm to display triangle as follows:
# 1
# 2 2 
# 3 3 3
# 4 4 4 4
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#17.Write a program to remove all punctuations from given string.
# input_string="!,hello!, how are you?&&"
# punctuation=''';;;[[]]\\\\!!!??&&&,,{}[]:;'''
# result_string=" "
# for char in input_string:
#     if char not in punctuation:
#         result_string+=char
        #thers is punctuations so no print for this
# print(result_string)


 # 19Write a program to count the no:of each vowel in a given string.
# string1=input("enter string:")
# vowels=0
# for i in string1:
#     if(i=="a" or  i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" ):
#         vowels+=1
# print("number of vowels are:")
# print(vowels)

#20. Program to perform Addition,Subtraction,Multiplication and division on Complex-No's.
# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))
# print(num1)
# print(num2)
# res=num1+num2
# print("\naddition result=",res)
# res=num1-num2
# print("\nsubstraction result=",res)
# res=num1*num2
# print("\nmultiplication result=",res)
# res=num1/num2
# print("\ndivision result=",res)

#21. Find Value of the following expressions

# num_1 = 10

# num_2 = 11

 

# num_1 % num_2

# num_1 - num_2

# num_1 * num_2
# num_1=10
# num_2=11
# res1=num_1%num_2
# print(res1)
# res2=num_1-num_2
# print(res2)
# res3=num_1*num_2
# print(res3)

# 22. Find the results of the following expressions (True or False)

# num_1=7

# num_2 = 6

 

# num_1 < num_2

# num_1 > num_2

# num_1 <= num_2

# num_1 >= num_2

# num_1=num_2

# num_1 = 10

# num_2 = 11
# res=num_1 < num_2
# print(res)








# 23. Find the results of the following expressions (True or False)

# num_1=3

# num_2 = 4

 

# (num_1 < num_2) and (num_1 != num_2)

# (num_2 >= num_1) or (num_1 > num_2)

# not (num_1 == num_2)

# num_1=3

# num_2 = 4
# res=(num_1 < num_2) and (num_1 != num_2)
# print(res)


# 24.  Output of the following while loop

# i=1

# while (i<6):

#     i = i +1

#    print(i)
# i=1

# while (i<6):
#     i = i +1
#     print(i)
 

#25. Select the correct option

 

# customer_num =5

# invoice_num =1212

# print("Invoice No(s):")

# while(customer_num >0):

#      print("INV -", invoice_num)

#      invoice_num = invoice_num +3

#      customer_num = customer_num -1
# customer_num =5

# invoice_num =1212

# print("Invoice No(s):")

# while(customer_num >0):

#      print("INV -", invoice_num)

#      invoice_num = invoice_num +3

#      customer_num = customer_num -1




 


