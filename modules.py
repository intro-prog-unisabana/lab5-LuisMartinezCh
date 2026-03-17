import os
import math

directorio_actual = os.getcwd()
print(f"Current working directory: {directorio_actual}")

num = int(input("Enter an integer:"))

def operacion_log (num):
    resultado = math.log2(num)
    ceiling = math.ceil(resultado)
    floor = math.floor(resultado)
    return resultado

def operacion_ceiling (num):
    resultado = math.log2(num)
    ceiling = math.ceil(resultado)
    floor = math.floor(resultado)
    return ceiling

def operacion_floor (num):
    resultado = math.log2(num)
    ceiling = math.ceil(resultado)
    floor = math.floor(resultado)
    return floor

resultado_log = operacion_log(num)
resultado_ceiling = operacion_ceiling(num)
resultado_floor = operacion_floor(num)
print(f"Log base 2 of {num} is: {resultado_log}")
print(f"Floor: {resultado_floor}")
print(f"Ceiling: {resultado_ceiling}")