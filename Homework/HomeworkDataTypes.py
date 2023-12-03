#Excersise 1 
#calculate the rectangle area

"""
        a
-------------------
|                 |
|                 |   b
|                 |
-------------------
"""
#define the side of the rectangle in sm 
a = 10
b = 5
print ("The are of the rectangle is :", a*b, "cm²")

#Excersise 2
#Print the name of the person with input variable

name = input("Please enter the name:")
print (f"Hello, {name} !")

#excersise 3 
#print First and Last name age and city you are living in 
fName  = input("Please enter you first name:")
lName = input("Please enter your last name:")
age = input("Please enter your age:")
town = input("Please enter the town where you living:")

print (f"Your name is {fName} {lName}\nYour age is {age}\nand you live in {town}")

#excersise 4
#Input date and printout the date + 1 year 
import datetime

dat = input("Please enter the date (YYYY-MM-DD)")
#dat = "2023-03-03"


date_object = datetime.datetime.strptime(dat, "%Y-%m-%d")
date_object = int((date_object.year) + 1) , int(date_object.month), int(date_object.day)
#print (type(date_object))

out = datetime.datetime(*date_object)
print ("The new date is : ", out)


# #excersise 5
#Declare 3 variables in type integer add into a list and print the sum 
val1 = input("First Integer:")
val2 = input("Second Integer:")
val3 = input("Third integer:")

list_val  = []
list_val.append(val1)
list_val.append(val2)
list_val.append(val3)

sum = 0

for i in range(len(list_val)):
    try:
        sum += int(list_val[i])
    except ValueError:
        print (f"The value [{list_val[i]}] cannot be other than int, ERROR!")

print (f"The sum of the input values is : {sum}")   

#excersise 6
#Generate a list of random numbers add them up and find the sum

#python does not have define function random so we import it 
import random

nummbers = random.randrange(1, 10)
sums = 0
list_array = []

#print (nummbers)
#print (range(nummbers))
#list_array.insert(0,(random.randrange(1, 9999)))

for i in range(nummbers):
    #print (i)
    list_array.insert(i, random.randrange(1, 9999))
    
#print (list_array)

for x in range(len(list_array)):
    #print (list_array[x]) 
    sums += int(list_array[x])

print (f"Random numbers count are [{nummbers}]
       \nThe numbers generated for each random count are {list_array}\nThe sum of these numbers is : [{sums}]")