# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

import pandas as pd

def read_data(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except:
        print(f"The file '{filename}' does not exist.")
        return None

# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem  #the problem is that in this line we are adding the original number 'elem' instead of 'double'

#this would be the correct code:

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string #the problem is that we are substituting the value 'strings' every time we enter the loop

#this would be the correct code:

strings = ''
for string in ['I', 'am', 'Groot']:
    if len(strings) > 0:
        strings = strings+"_"+string
    else:
        strings = string

### (c) Careful!
j=10
while j > 0:
   j += 1  #this leads to an infinite loop, as j will always be bigger than 0

#we should set a way to stop it, such as below:

j=10
while j < 100:
    j+=1

### (d)
productory = 0 #since we initiate the variable at 0, any further multiplication will always just be 0
for elem in [1, 5, 25]:
    productory *= elem

#we should set 'productory' equal to 1

productory = 1
for elem in [1, 5, 25]:
    productory *= elem


