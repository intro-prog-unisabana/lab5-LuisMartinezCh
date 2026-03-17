def promedio_estudiante(*num):
    total = 0
    for digit in num:
        total += digit
        return total/(len(num))

print(promedio_estudiante())
