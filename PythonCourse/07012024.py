# # def factoriel(n):
# #     if n == 0:
# #         return 1 
# #     else:
# #         return    ( n * factoriel(n -1 ))
# # print (factoriel(3))


# # def rev(s):
# #     for i in s:
# #         str = str(i) + str(str)
# #     return str
# # print (rev('1234abvg'))



import re
def cnt(x):
    c = 0
    l = 0
    for i in x :
        if i.isupper():
            c = c +1 
        elif i.islower():
            l = l + 1 
    num = len(re.findall("[0-9]",x))
    #print (len(x))
    spc = len(x) - (c+l+num)        
    return print (f"Capital Letters are: {c}, Lowercase {l} , Numbers are {num}, Special Char : {spc}") 

s = cnt("BoaynBaykov123@ !!!") 

print (s)

# # for ss in s:
# #     print (if range(),ss )
    
# # print (cnt("BoaynBaykov123@"))



# # def factorial(n): 
     
# #     # Checking the number
# #     # is 1 or 0 then
# #     # return 1
# #     # other wise return
# #     # factorial
# #     if (n==1 or n==0):
         
# #         return 1
     
# #     else:
# #         print (n)
# #         return (n * factorial(n - 1)) 
 
# # # Driver Code 
# # num = 5; 
# # print("number : ",num)
# # print("Factorial : ",factorial(num))

 
# x = lambda a : a + 15 
# print (x(2))


# ab = [1,2,3,3,3,4,5]

# def max_val(x):
#     return max(x,key=x.count)

# print (max_val(ab))

# def other_fun (a,b):
#     sq = a*2
#     def add (a,b):
#         return a + b
#     add = add(a,b)
#     return add + sq

# result = other_fun(5,10)
# print (result)