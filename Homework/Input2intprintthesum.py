num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

def tryParseIntFloat(val):
    try:
        res = int(val)
        return res
    except ValueError:
        try:
            res = float(val)
            return res
        except ValueError:
            return None

if num1.find(",") != -1:
       num1 = num1.replace(",",".")
       print (f"You are trying to use comma [,] beside dot [.] - string replaced with correct values")

if num2.find(",") != -1:
       num2 = num2.replace(",",".")
       print (f"You are trying to use comma [,] beside dot [.] - string replaced with correct values")

if tryParseIntFloat(num1) != None:
    number1 = tryParseIntFloat(num1)
else:
    print (f"incorrect value for First value [{num1}], please enter a valid number ")

if tryParseIntFloat(num2) != None:
    number2 = tryParseIntFloat(num2)
else:
    print (f"incorrect value for Second value [{num2}], please enter a valid number ")
        
if tryParseIntFloat(num2) is not None and tryParseIntFloat(num1) is not None:
    try:
        sum = number1+number2
        print("Sum of the both numbers is :", sum)
    except ValueError as e:
        print(f"Error: {e}")
else:
    print ("Error!")