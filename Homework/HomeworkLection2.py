#define 2 variable 
#first one integer 
#second one float 

#devide first value to second

val1 = 10
val2 = 2.5

#solution 
devide = val1 / val2
print (f"Devide [{val1}] / [{val2}] is :", devide)

#concat 3 values - my fullname 

fName = "Boyan"
mName = "Hristov"
lName = "Baykov"
print (fName+" " +mName+" " +lName)

#Print each of my name in separate row with single print 
print("My Full Name is :\n", fName, "\n",mName, "\n",lName )

#define 2 arrays - list and dictionary with at least 5 values 

list_array = ["list1", "list2", "list3", "list4", "list5"]
dict_array = {"val1" : "first", "val2":"second", "val3":"third", "val4":"forth", "val5":"fifth"}

#print valuue before last one for each array
print (list_array[-2])

#WIP - work in progress get the last dictionary word 
#print (list(dict_array.keys())[-2])

print(dict_array[list(dict_array.keys())[-2]])