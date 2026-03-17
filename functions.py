def promedio_estudiante(valores):
    if valores is None or len(valores) == 0:
        return 0.0
    total = 0.0
    for v in valores:
        total += v
    return total / len(valores)

print(promedio_estudiante([85, 92, 78]))

