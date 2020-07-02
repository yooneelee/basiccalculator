def calculator(num1, num2, operator):
    
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    if operator == 1:
        print('Solution: ', + addition)
    elif operator == 2:
        print('Solution: ', + subtraction)
    elif operator == 3:
        print('Solution: ', + multiplication)
    elif operator == 4:
        print('Solution: ', + division)
    else:
        print('ERROR WRONG INPUT')

print("Python Project #1: Basic Calculator")
print("Operator List: ")
print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")
numberOne = int(input("First value: "))
numberTwo = int(input("Second value: "))
operator = int(input("Math operator: "))

product = calculator(numberOne, numberTwo, operator)
    
    
    