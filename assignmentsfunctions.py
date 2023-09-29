#1.Write a program to define a function that can accept an integer number as    input and print the "It is an even number" if the number is even, otherwise print "It is odd".
# def Checkevenodd(num):
#     if(num%2==0):
#         print(num,"is even")
#     else:
#         print(num,"is odd")
# Checkevenodd(7)
# Checkevenodd(10)
# Checkevenodd(11)
# Checkevenodd(16)

#2. Write a program to define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# def generate_dict(num):
#     d=dict()
#     for num in range(1,num+1):
#         d[num]=num*num
#     return d
# result=generate_dict(7)
# print(result)

#3. Write a program to take a string as input and return a string with vowels removed.(implement List Comprehesion)
# text=input("enter a string:")
# vowels=["a","e","i","o","u"]
# newtext=""
# textlen=len(text)
# for i in range(textlen):
#     if text[i] not in vowels:
#         newtext=newtext+text[i]
# print("\nString after removing vowels")
# text=newtext
# print(text)

#4.Write a program to display Powers of 2  using Anonymous functions?(lambda,map).
# terms=8
# result=list(map(lambda x:2**x,range(terms)))
# print("total terms are:",terms)
# for num in range(terms):
#     print("2 raised to power",num,"is",result[num])

#7. Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.
# def create_dict(values,keys):
#     return dict(zip(values,keys))
# key_list=[1,2,3,4,5]
# value_list=["apple","banana","kiwi","blueberry","strawberry"]
# result=create_dict(key_list,value_list)
# print(result)

#8.Write a program to print fibonocci series using function.
# def fibonacci(n):
#     fibonacci_series=[]
#     a,b=0,1
#     while len(fibonacci_series)<n:
#         fibonacci_series.append(a)
#         a,b=b,a+b
#     return fibonacci_series
# n=int(input("enter a number:"))
# result=fibonacci(n)
# print("fibonacci series")
# for num in result:
#     print(num,end="")




#11. Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.(implement generator).
# def NumGenerator(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i
# n=int(input("enter number"))
# values=[]
# for i in NumGenerator(n):
#     values.append(str(i))
# print(",".join(values))

#12.Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.(implement generator)
# def NumGenerator(n):
#     for i in range(n+1):
#         if i%2==0:
#             yield i
# n=int(input("enter a number"))
# values=[]
# for i in NumGenerator(n):
#     values.append(str(i))
# print(",".join(values))

#16. Write a Python program to find the second smallest number in a list using function.
# def second_smallestnum(nums):
#     if len(nums)<2:
#         return "the list must contain atleast two elements"
#     smallest=second_smallestnum=float("inf")
#     for num in nums:
#         if num<smallest:
#             second_smallestnum=smallest
#             smallest=num
#         elif num<second_smallestnum and num!=smallest:
#             second_smallestnum=num
#     if second_smallestnum==float("inf"):
#         return "there is no second smallest number in the list"
#     return second_smallestnum
# my_list=[2,3,4,5,6,7,8,9]
# result=second_smallestnum(my_list)
# if isinstance(result,int):
#     print(f"the second smallest number is:{result}")
# else:
#     print(result)

#5. Write a program to implement bubble-sort algorithm
# def bubblesort(arr):
#     n=len(arr)
#     swapped=False
#     for i in range(n-1):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 swapped=True
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#         if not swapped:
#             return
# arr=[65,34,25,12,22,11,90]
# bubblesort(arr)
# print("sorted array is:")
# for i in range(len(arr)):
#     print("%d" % arr[i],end=" ")


#9. Write a program to find the factorial of a number using function.
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x*factorial(x-1))
# num=int(input("enter number:"))
# result=factorial(num)
# print("the factorial of num",num,"is",result)

#14. Program to implement Linear-Search Algorithm.
# def linearsearch(array,n,x):
#     for i in range(0,n):
#         if(array[i]==x):
#             return i
#     return -1
# array=[2,4,6,8,10]
# x=4
# n=len(array)
# result=linearsearch(array,n,x)
# if(result==-1):
#     print("element is not found")
# else:
#     print("element is found at index: ",result)

#15. Program to implement Selection-Sort Algorithm.
# def selctionsort(array,size):
#     for ind in range(size):
#         min_index=ind
#         for j in range(ind+1,size):
#             if array[j]<array[min_index]:
#                 min_index=j
#         (array[ind],array[min_index])=(array[min_index],array[ind])
# arr=[-2,45,0,11,-9,88.-97,-202,747]
# size=len(arr)
# selctionsort(arr,size)
# print("the array in ascending order after selcetion order is :")
# print(arr)

#6. Write a program to implement binary-search algorithm
# def binarysearch(array,x,low,high):
#     while low<=high:
#         mid=low+high//2
#         if array[mid]==x:
#             return mid
#         elif array[mid]<x:
#             low=mid+1
#         else:
#             high=mid-1
# array=[3, 4, 5, 6, 7, 8, 9]
# x=4
# result=binarysearch(array,x,0,len(array)-1)
# if result!=-1:
#     print("element is present at index "+str(result))
# else:
#     print("not found")



















    


















        
    



