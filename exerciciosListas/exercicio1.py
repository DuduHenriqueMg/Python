lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52];
numeros_pares = [];
ocorrencias = 0;
soma = 0;

for numero in lista:
    if numero % 2 == 0:
        numeros_pares.append(numero);
    if numero == lista[0]:
        ocorrencias = ocorrencias + 1;
    if numero < 0:
        soma = soma + numero
    

print(f"Maior número da lista: {max(lista)}");
print(f"Menor número da lista: {min(lista)}");
print(f"Números pares:{numeros_pares}");
print(f"Ocorrencias do primeiro elemento da lista: {ocorrencias}");
print(f"Soma dos números negativos da lista: {soma}");
print(f"Média dos números da lista:{sum(lista) / len(lista)}");