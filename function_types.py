flotantes = [100.0, 200.0, 300.0]
def list_shift(a, b):
    for i in range(len(a)):
        a[i] += b
    return a

def calc_avg(a):
    prom = sum(a)/len(a)
    return prom

def print_normalized (a):
    return a


print(list_shift(flotantes, 25))
print(calc_avg(flotantes))
print(print_normalized(flotantes))