import math

def combinaciones(n, r):
    if r < 0 or r > n:
        return 0
    

    return math.comb(n, r)

n = 7
r = 3

resultado = combinaciones(n, r)

print(f"El número total de elementos (n) es: {n}")
print(f"El número de elementos a elegir (r) es: {r}")
print(f"El número de combinaciones C({n}, {r}) es: {resultado}")