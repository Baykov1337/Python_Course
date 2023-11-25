dict_array1 = {"val1" : "first", 
              "val2":"second", 
              "val3":"third", 
              "val4":"forth", 
              "val5":["fifth", "six", "seven"]}

#print (dict_array1[list(dict_array1.keys())[-1]][:1:-1])

print (list(dict_array1.keys()))
print (list(dict_array1.values()))

print (dict_array1.items())


# for keys, value in dict_array1.items():
#     if isinstance(value, list):
#         for i in keys[list()]:
#             print (value[list(value.keys())[i]])




#for keys, value in dict_array1.items():
 #   if isinstance(value, list):
 #       for i in range(len(value)):
 #           print (keys[i]) 
   # print (keys)

    #for i in value.keys():
      

#my_fullname = ["Boyan", "Hristov", "Baykov"]

#print (range(len(my_fullname)))
#for i in range(len(my_fullname)):
#    print(my_fullname[i])