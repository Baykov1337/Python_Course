#write function that accepts 3 numbers and returs the lowest one
count = 0
list_numbers = []

while count < 3:
        new_val = 0 
        input_number = input("Please input single number:")
        try:
           new_val = int(input_number)
        except:
            print (f"The input value [{input_number}] is not an integer, please enter integer value! ")
        count = count+ 1
        list_numbers.append(new_val)


def integer_input_return_lowest(numbers):
    return min (numbers)

print (f"The lowest number from {list_numbers} is {integer_input_return_lowest(list_numbers)}")

#write function that will accept 3 int values - 1st 2 number will be sum 

# def sum_numbers(list_numbers):
#      return (list_numbers[0] + list_numbers[1])

#depending how you interpretate the task it could be like this 
int_value1 = list_numbers[0]
int_value2 = list_numbers[1]
int_value3 = list_numbers[2]

def sum_numbers(int_value1, int_value2):
    if type(int_value1) == int and type(int_value2) == int:
         return (int_value1 + int_value2)
    else:
         return print ("The value of 1st 2 numbers is not integer!")

def substract(number1, number2):
    if type(number1) == int and type(number2) == int:
         return (number1 - number2)
    else:
         return print ("The value of 1st 2 numbers is not integer!")

def add_and_subtract(value1, value2, value3):
     return substract(sum_numbers(value1, value2),value3)


print (f"The result of add and substact is : {add_and_subtract(int_value1, int_value2 ,int_value3 )}")

#input string with single spaces return only even number from that list

input_strting = input("Please enter the string with numbers separated with single spaces. ")
list_input_string_output = []

list_input_string = [int(x) for x in input_strting.split()]

def is_even_number(value):
  if (int(value) % 2) == 0 :
    return True
  else:
    return False

result = filter(is_even_number, list_input_string)

for x in result:
    list_input_string_output.append(x)

print (list_input_string_output )  

#write program that accept values with single spaces and sort them

input_strting = input("Please enter the string with numbers separated with single spaces. ")
list_input_string_output = []

list_input_string = [int(x) for x in input_strting.split()]

sorted_values = sorted(list_input_string)

print (sorted_values)

#write program that accept values with single spaces and print max number min number and sum 

input_strting = input("Please enter the string with numbers separated with single spaces. ")
list_input_string_output = []

list_input_string = [int(x) for x in input_strting.split()]

max_values = max(list_input_string)
min_values = min(list_input_string)
sum_values = sum(list_input_string)
print (f"The minimum number is {max_values}")
print (f"The minimum number is {min_values}")
print (f"The minimum number is {sum_values}")