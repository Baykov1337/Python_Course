class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)
    
    @staticmethod
    def multiply(*args):
        result = 1
        if len(args) == 1:
            raise ValueError("You cannot multiply single number")
        for i in args:
            result = result * i
        return result
    
    @staticmethod
    def divide(*args):
        if len(args) < 1:
            raise ValueError ("The function divide needs at least 2 arguments!")
        
        result = args[0]
        for i in args[1:]:
            if i == 0:
                raise ValueError("Devide by zero not allowed!")
            result /= i 
        return result
    
    @staticmethod
    def subtract(*args):
        if len(args) == 0:
            raise ValueError("For substract you need at least 2 values.")
        
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 4))
print(Calculator.divide(100, 2,2,12.5))
print(Calculator.subtract(90, 20, -50, 43, 7))