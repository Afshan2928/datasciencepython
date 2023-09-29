# 1. Programs to implement the concept of calendar module.
# import calendar
# yy=2017
# mm=11
# print(calendar.month(yy,mm))

#2. Write Programs to implement datetime module ?
# from datetime import date
# my_date=date(1996,12,11)
# print("date passed in argument",my_date)

# 5. Write a program to implement math module ?
# import math
# r=4
# pie=math.pi
# print(pie*r**2)

# 4. Write a program to implement operator module
# import operator
# x=int(input("enter first integer"))
# y=int(input("enter second integer"))
# addresult=operator.add(x,y)
# print("result",addresult)

#3. Write Programs to implement time module (includes formatting) ?
# import time

# # Get the current time in seconds since the epoch (January 1, 1970)
# current_time = time.time()
# print(f"Current time in seconds since the epoch: {current_time}")

# # Convert the current time to a struct_time object
# current_struct_time = time.localtime(current_time)
# print(f"Current time as a struct_time object: {current_struct_time}")

# # Format the current time as a string
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_struct_time)
# print(f"Formatted time: {formatted_time}")

# # Sleep for 2 seconds
# print("Sleeping for 2 seconds...")
# time.sleep(2)
# print("Woke up!")

# # Measure the time it takes to execute a code block
# start_time = time.time()
# for i in range(1000000):
#     pass
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Time taken to execute the loop: {elapsed_time} seconds")
