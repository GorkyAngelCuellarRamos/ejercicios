# Programa: término n-ésimo y suma de n términos de una PA

a1 = float(input("Ingresa el primer término (a1): "))
d = float(input("Ingresa la diferencia (d): "))
n = int(input("Ingresa el número de términos (n): "))

an = a1 + (n - 1) * d
print("El término número", n, "de la progresión aritmética es:", an)

Sn = n * (a1 + an) / 2
print("La suma de los", n, "primeros términos es:", Sn)