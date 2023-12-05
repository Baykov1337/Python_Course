#write program that accept input 2 int values and print the bigger one.
val = input("Please enter the int val:")
val1 = input("Please enter the int val:")

try:
    int(val)
except ValueError:   
    print ("You've entered incorrect value!") 
try:
    int(val1)
except ValueError:   
    print ("You've entered incorrect value!") 

if val > val1:
    print (val)
else:
     print (val1)

#write code that accept 2 imputs sex and age

sex = input("Please enter your Sex (m/f): ")    
age = input("Please enter your age :")

try:
    sex  in ("m","f")
except ValueError:   
    print ("You've entered incorrect value!") 
try:
    int(age)
except ValueError:   
    print ("You've entered incorrect value!") 

if age >=16 and sex == "m":
    print ("Mr.")
if age <16 and sex == "m":
    print ("Master")   
if age >=16 and sex == "f":
    print ("Ms.")   
if age <16 and sex == "f":
    print ("Miss.")   
     

#write program that after input will display if the number is odd or even

num = input("Please enter the number : ")

try:
    int(num)
except ValueError:   
    print ("You've entered incorrect value!") 
num = int(num)
if (num % 2)  == 0: 
    print ("even")
else:
    print ("odd")    

#write code that accept input parameter as string a day of the week and return the price of a ticket

day = input("Please enter the day of the week: ")

if day not in ("Moonday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
    print ("The day you entered is invalid")
    exit()

if day == "Moonday":
    print (f"The price of the ticket for {day} is 12")
elif day == "Tuesday":
    print (f"The price of the ticket for {day} is 12")
elif day == "Wednesday":
     print (f"The price of the ticket for {day} is 14")
elif day == "Thursday":
     print (f"The price of the ticket for {day} is 14")     
elif day == "Friday":
     print (f"The price of the ticket for {day} is 12")    
elif day == "Saturday":
     print (f"The price of the ticket for {day} is 16") 
elif day == "Sunday":
     print (f"The price of the ticket for {day} is 16")      