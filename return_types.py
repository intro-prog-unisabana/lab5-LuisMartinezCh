def obtener_precio_usuario(precio):
    precio_float = float(precio)
    return (precio_float)
precio = input("Enter the item's price:\n")
precio_final = obtener_precio_usuario(precio)
print(precio_final)