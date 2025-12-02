import math

def permutaciones(n, r):
    return math.perm(n, r)

n = 10 
r = 4   

# Calcular las permutaciones
resultado = permutaciones(n, r)

# Mostrar el resultado
print(f"El número de maneras en que se pueden sentar las personas es: {resultado}")