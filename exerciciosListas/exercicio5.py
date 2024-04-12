lista = [9, 8, 7, 12, 0, 13, 21];
pares = [];
impares = [];

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero);
    else:
        impares.append(numero);
        
print(f"Números pares:{pares}");
print(f"Números impares:{impares}");
