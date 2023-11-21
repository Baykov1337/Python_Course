#define 2 variable #first one integer #second one float 
#divide first value to second

val1 = 10
val2 = 2.4

#solution 
divide = val1 / val2
print (f"Divide [{val1}] / [{val2}] is :", divide)

#divide 2 values with result as whole number
print (val1//val2)

#concat 3 values - my fullname 
fName = "Boyan"
mName = "Hristov"
lName = "Baykov"
print (fName+" " + mName + " " +lName)
 
#Print each of my name in separate row with single print 
print("My Full Name is :\n", fName, "\n",mName, "\n", lName )

#define 2 arrays - list and dictionary with at least 5 values 
list_array = ["list1", "list2", "list3", "list4", "list5"]
dict_array = {"val1" : "first", 
              "val2":"second", 
              "val3":"third", 
              "val4":"forth", 
              "val5":"fifth"}

#print value before last one for each array
print (list_array[-2])

#WIP - work in progress get the last dictionary word 
#print (list(dict_array.keys())[-2])
#the result
print(dict_array[list(dict_array.keys())[-2]])