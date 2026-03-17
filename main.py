from utils_calc import *
resultdo = None
while True:
    operation = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):")
    print(operation)
    if operation == "add":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (add(num1,num2))
        print(f"The result is: {resultdo}")
    if operation == "subtract":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (sub(num1,num2))
        print(f"The result is: {resultdo}")
    if operation == "multiply":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (multiply(num1,num2))
        print(f"The result is: {resultdo}")
    if operation == "divide":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (divide(num1,num2))
        print(f"The result is: {resultdo}")
    if operation == "exponent":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (exponent(num1,num2))
        print(f"The result is: {resultdo}")
    if operation == "modulo":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (modulo(num1,num2))
        print(f"The result is: {resultdo}")
    if operation == "floor_divide":
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
        resultdo = (floor_divide(num1,num2))
        print(f"The result is: {resultdo}")
    if operation == "absolute":
        num1 = int(input("Enter the first number:"))
        resultdo = (absolute(num1))
        print(f"The result is: {resultdo}")
    if operation == "exit":
        break
    elif operation != "add" and operation != "subtract" and operation != "multiply" and operation != "divide" and operation and "exponent" and operation != "modulo" and operation != "floor_divide" and operation != "absolute" and operation != "exit":
        print("Invalid option!")

