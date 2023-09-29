#10. Write a program to implement List Comprehension
# fruits=["apple","banana","orage","kiwi"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)

#11. Write a program to implement Dictionary Comprehension
# fruits={"apple":9,"mango":5,"kiwi":7}
# newdict=[x for x in fruits if "a" in x]
# print(newdict)

#12.Write a program to find the largest and smallest element from a list
# mylist=[78,63,28,16,89]
# largest_num=mylist[0]
# smallest_num=mylist[0]
# for num in mylist:
#     if num>largest_num:
#         largest_num=num
#     elif num<smallest_num:
#         smallest_num=num
# print(f"largest num:{largest_num}")
# print(f"smallest number:{smallest_num}")

#13. Write a Python program to print the numbers of a specified list after removing even numbers from it.
# my_list=[1,2,3,4,5,6,7,8,9]
# oddnum=[num for num in my_list if num%2!=0]
# print(my_list)

#14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30
# square=[num**2 for num in range(1,31)]
# first_five=square[:5]
# last_five=square[-5:] #because the position of colon
# print("first five numbers are:",first_five)
# print("last five numbers are:",last_five)

#15.Write a Python program to insert a given string at the beginning of all items in a list.
# list1=[1,2,3,4,5]
# list1[0]="hello"
# print(list1)
# list1.insert(1,1)
# print(list1)

#16.Write a Python program to iterate over two lists simultaneously.
# list1=[1,2,3,4]
# list2=["d","e","f","g"]
# for item1,item2 in zip(list1,list2):#we can change variables
    # print(item1,item2)

#1. Write a program to find the transpose of a matrix using nested loop
# x=[[12,4],
#    [5,6],
#    [3,8]]
# result=[[0,0,0],
#         [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i]=x[i][j]
# for r in result:
#     print(r)

#2. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# str1="hello How ARE YOU"
# str2=str1.capitalize()
# print(str2)

#3.Write a program to implement all built-in methods of list.
# list1=[1,3,4,5,6,7]
# print(list1[0])
# print(list1[:])
# del list1
# list1[5]=9
# print(list1)


#4.Write a program to read dictionary values through keyboard and merge two dictionaries.
# dict1={"id":"afshan","year":21,"number":163}
# dict2={"name":"nara","age":20,"height":175}
# merged_dict=dict1|dict2
# print(merged_dict)

#5.Write a program to demonstrate all built-in methods of dictionary.
# dict1={"name":"inu","age":54,"salary":34000}
# print(len(dict1))
# dict2=str(dict1)
# print(dict2)
# print(dict1.values())
# print(dict1.keys())
# print(dict1.items())
# print(dict1.clear())

#6. Write a program to find the sum of all the elements in a list.
# total=0
# list1=[11,5,6,7,8]
# for ele in list1:
#     total=total+ele
# print("sum of elements",total)

#7. With a given integral number n, write a program to generate a dictionary that contains(i,i*i) such that i is an integral number between 1 and n. And then the program should print the dictionary.
# n=int(input("enter a number:"))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)

#17. Write a Python program to add a key to a dictionary.
# my_dict1={"fruit":"mango","vegetable kg":6}
# my_dict1["city"]="jaipur"
# print(my_dict1)

#18.Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50,6:60}
# dict1={1:10, 2:20}
# dict2={3:30, 4:40}
# dict3={5:50, 6:60}
# concatenated_dict={**dict1,**dict2,**dict3}
# print(concatenated_dict)

#19.Write a Python program to iterate over dictionaries using for loops.
# dict1={"name":"alana","age":43,"city":"jaipur"}
# for key in dict1:
#     print(key)
# for values in dict1:
#     print(values)
# for key,values in dict1.items():
#     print(key,values)

#20.Write a Python program to sum all the items in a dictionary.
# dict1={"lemon":10,"apple":23,"orange":32}
# total_sum=0
# for value in dict1.values():
#     total_sum+=value
# print("sum of all items in the given dictionary:",total_sum)

# 21.Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.Eg : {'Dog':'Willie'} Put at least 3 key-value pairs in your dictionary. Use a for loop to print out a series  statements such as "Willie is a dog"
# Create a dictionary of pets 
# pets={"willie":"dog","nemo":"fish","greeny":"parrot"}
# for pet_name,pet_type in pets.items():
#     print(f"{pet_name} is a {pet_type},")

#22. Write a python function to create and return a new dictionary from the given dictionary (subject: mark).

# Create a new dictionary with subject having marks more than 50.
# marks = {English: 40,'Maths': 60, 'Hindi: 30,'Chemistry': 46,'Physics': 70}

# def markdict(original_dictionary):
#     passed_sunjects={}
#     for subject,mark in original_dictionary.items():
#          if mark>50:
#              passed_sunjects[subject]=mark
#     return passed_sunjects
# sample_dictionary={"English": 40,'Maths': 60, "Hindi": 30,'Chemistry': 46,'Physics': 70}
# passed_subjects_dictionary=markdict(sample_dictionary)
# print(passed_subjects_dictionary)


#23. Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.It should return a dictionary in which the key should be letter count and value should be digit count. Ignore the spaces or any other special character in the sentence.
# str1=input("input a string:")
# d=a=0
# for i in str1:
#     if i.isdigit():
#         d=d+1
#     elif i.isalpha():
#         a=a+1
#     else:
#         pass
# print("letters",a)
# print("dogitis",d)

# 24. Write a Python function which generates and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.
# d=dict()
# n=43
# for i in range(1,n+1):
#     d[i]=i**2
# print(d)
 






    




















#2. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.


