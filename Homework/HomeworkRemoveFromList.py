#homework - remove all values that can be divided to 2 

#1st solution w/o loop  
str1 = 'BoYaNhRiStOv' #an example 
list_str1 = list(str1)
print (list(str1))

print (list(str1)[0])
# 
# 
#  in the list 1st value is 0 2nd is 1 and so on  - but 0 is even number - so if we count like regulat math it should be 1,3,5,7,9... in a program language .. to be discussed further

list_str1.remove(list(str1)[1]) 
list_str1.remove(list(str1)[3]) 
list_str1.remove(list(str1)[5]) 
list_str1.remove(list(str1)[7]) 
list_str1.remove(list(str1)[9]) 
list_str1.remove(list(str1)[11]) 
print (list_str1)

#finaly if we want to concat values in the list 
print ("".join(list_str1))

#2nd solution 
str1 = 'BoYaNhRiStOv' #an example
# print (str1[1])
new_str = ""
print (len(str1))

for x in range(len(str1)):
    if (x % 2) == 0:
        print (x)
        new_str += str1[x]

print (new_str)
