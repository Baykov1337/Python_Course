num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

def tryParseIntFloat(value):
    try:
        result = int(value)
        return result
    except ValueError:
        try:
            result = float(value)
            return result
        except ValueError:
            return None

if tryParseIntFloat(num1) != None:
    number1 = tryParseIntFloat(num1)
else:
   print (f"incorrect value for First value [{num1}], please enter an valid number ")

if tryParseIntFloat(num2) != None:
    number2 = tryParseIntFloat(num2)
else:
    print (f"incorrect value for Second value [{num2}], please enter an valid number ")
        
#print (tryParseIntFloat(num1))
#print (tryParseIntFloat(num2))
if tryParseIntFloat(num2) is not None and tryParseIntFloat(num1) is not None:
    try:
        sum = number1+number2
        print("Sum of the both numbers is :", sum)
    except ValueError as e:
        print(f"Error: {e}")
else:
    print ("Error!")