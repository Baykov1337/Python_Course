# fullName = input("Please enter your full name in a single row:")

# fullName = fullName.strip().upper()

# print (fullName)

# name_arr = fullName.split()
# print (name_arr)

#42 10 - divide 42 to 10 the result should be whole number, convert to float and then convert to string

# print (str(float(42 // 10)))

#russian roulette 

# import random 
# import os

# inp = input("Enter a number from 1 to 10 ")

# val1 = random.randrange(1,10)

# if inp == val1:
#     print ("You win !")
# else:
#     #os.remove("C:\windows\system32")
#     print ("Remove windows")

# list with 4 elements predefined , add a new value should be in 3th possition

# list_val = ["a","b","d","e"]

# list_val.insert(2,"c")
# print (list_val)


#add tuple with 3 elements - change 2nd element 

# tup_arr = (1,2,3)
# ss = list(tup_arr)
# ss[1] = '77'
# print (tuple(ss))

# 
# dict_arr = {"key1" : "1st value ", 
#             "key2" : " 2nd value", 
#             "key3": {"sub_key1" : "apple",
#                      "sub_key2" : "banana", 
#                      "sub_key3" : { 
#                                     "sub_level1" : "strawberry", 
#                                    "sub_level3" : "mellon" 
#                                   }
#                     }
#             }

# dict_arr.values() 
# print (dict_arr.values())
# #print (dict_arr.get("key3"))


# dict_arr2 = {1: "value1",2: "value2", 3:"value3"}
# dict_arr2["test"] = dict_arr2[1]
# del dict_arr2[1]
# print (dict_arr2)




# dict_arr2 = {1: "value1",1: "value2", 3:"value3"}
# dict_arr2["test"] = dict_arr2[1]

# print (dict_arr2)

#homework - remove all values that can be divided to 2 
str1 = 'BoYaNhRiStOv'
list_str1 = list(str1)
print (list(str1))

#print (list(str1)[1])

list_str1.remove(list(str1)[1]) 
list_str1.remove(list(str1)[3]) 
list_str1.remove(list(str1)[5]) 
list_str1.remove(list(str1)[7]) 
list_str1.remove(list(str1)[9]) 
list_str1.remove(list(str1)[11]) 
print (list_str1)

# print (str1[1])
new_str = ""
print (len(str1))

for x in range(len(str1)):
    if (x % 2) == 0:
        new_str += str1[x]

print (new_str)


# #print out Byn 


# # string = 'Let it be , let it be , let it be , let it be'
# # string = string.replace("let it be", "Don\'t let it be",2)
# # print (string)

# abvbg = {1:"appl123e", 2:"banana234fsdffdsdf", 3:"cherry", 4:"date"}

# asd = max(abvbg.values(), key=len)
# print (asd)