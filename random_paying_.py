import random

print("welcome to the random name generator for paying bills")
name = input("Enter all the name separated by coma ',' \n")
#This will split your name in list
name_split = name.split(',')
#print(f"your name in list form {name_split}")
length = len(name_split)

#print(f"length of your list is: {len(name_split)} ")
#genrate random number between 0 to length-1
random_digit = random.randint(0, length - 1)

#print(f"random genrated number is: {random_digit}")
#print(name_split[random_digit])
print(f"{name_split[random_digit]} is going to pay the bill")
