# write code that print fizzbuzz - if the number 
#could be divided by 3 fizz / 5 buzz if number could be devided by both 3 and 5 print fizzbuzz

# for i in range(51):
#     if (i % 3) == 0 and (i % 5) == 0:
#         print (f'{i} : FizzBuzz')
#     elif (i % 3) == 0:
#         print ((f'{i} : Fizz'))
#     elif (i % 5) == 0:
#         print ((f'{i} : Buzz'))
        

# input_val = input('Enter Value :')

# try:
#     val = int(input_val)
#     print (f'The value is Int : {input_val}')
# except ValueError:
#         try:
#             val = float(input_val)
#             print (f'The value is Float : {input_val}')
#         except ValueError:
#              print (f'The value is {input_val} string')

# asd = input ('Number:')
# to_int = int (asd)
# if (to_int > 100 and (to_int % 10) == 0)  or (to_int < 10 and (to_int % 2) == 0):
#     print ('True')
# else:
#     print ('False')

# list_list = []
# for i in range(1500,2701):
#     if (i % 5) == 0 and (i % 7) == 0:
#         list_list.insert(i, str(i))
# print (list_list)

# # s = ','.join(str(x) for x in list_list)
# # print (s)

# s = "____________".join(list_list)
# print (s)

# count even and odd numbers

# typle = (1,2,3,4,5,6,7,8,9)
# count_odd = 0
# count_even = 0

# for x in typle:
#     if not (x % 2) == 0:
#         count_odd = count_odd + 1
#         print (f"odd numbers: {x}") 
#     elif not (x % 2) != 0:
#         count_even = count_even + 1 
#         print (f"even numbers: {x}") 
# print (f"Count of odd numbers is : {count_odd}")      
# print (f"Count of even numbers is : {count_even}")     


# the password hould be between 6 and 12 symbols

# password = input("Please enter your passwor:")
# regex = ["!" ,"@" ,"#" ,"$" ,"%" ,"^" ,"&" ,"*" ,"(" ,")" ,"_" ,"+" ]
# spc_char = False
# val_true = False
# pas_len = False 
# if len(password) > 6 and len(password) < 12:
#     for x in password:
#         if x in regex:
#             spc_char = True
#         if x.isupper():
#             val_true = True
       
# else:
#     pas_len = True    
#     print ("The password should be more than 6 symbols and less than 12")

# if spc_char== False:
#     print ("The password should contail at least one special char")

# if val_true == False:
#     print ("The password should contrain at least 1 capital letter")


# # print ( pas_len, spc_char, val_true)
# if (pas_len == True or spc_char == False or val_true == False):
#     exit()
    
# conf_pass = input("Please confirm the passwod")

# if conf_pass == password:
#     print ("Password confirmed")  
# else:
#     print ("Password does not match")


# # list 5 cities 
input = input("Please enter a City: ")
city = ["stara zagora", "plovdiv", "sofia", "ruse", "varna"]

convert_low_input  = input.lower()

for i in input:
    if i.isupper():
        print ("There is upper letter")
        break

if convert_low_input in city:
    print ("The city exists")
else:
    print ("The city does not exists")

# homework - 

#input int - check if bool - da printo bool ili ne e , da se poveri da ne se deli na 5 ili na 3 
