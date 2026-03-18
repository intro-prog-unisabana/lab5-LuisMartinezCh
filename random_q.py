import random
random.seed(123)
a = int(input("Enter the start value:\n"))
b = int(input("Enter the end value:\n"))

entero_aleatorio = random.randint(a , b)
print(f"Generated random number: {entero_aleatorio}")

