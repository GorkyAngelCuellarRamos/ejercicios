def combinaciones_manual(n, r):
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1

    if r > n // 2:
        r = n - r

    numerador = 1

    for i in range(r):
        numerador *= (n - i)
    

    denominador = 1
    for i in range(1, r + 1):
        denominador *= i
        
    return numerador // denominador 
n = 35
r = 3
resultado_manual = combinaciones_manual(n, r)

print(f"\nResultado con la función manual: {resultado_manual}")