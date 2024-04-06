import math

a = float(input("Insira o coeficiente 'a': "))
b = float(input("Insira o coeficiente 'b': "))
c = float(input("Insira o coeficiente 'c': "))

delta = b**2 - 4*a*c

if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes da equação são: x' = {x1} e x'' = {x2}")
else:
    parte_real = -b / (2*a)
    parte_imaginaria = math.sqrt(-delta) / (2*a)
