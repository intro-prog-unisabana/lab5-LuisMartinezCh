datos = [2.0, 4.0, 6.0, 8.0]
def list_shift(a, b):
    for i in range(len(a)):
        a[i] += b
    return a

def calc_avg(a):
    prom = sum(a)/len(a)
    return prom

def print_normalized (a):
    return a


prom = calc_avg(datos)         
list_shift(datos, -prom)    
print_normalized(datos) 

