lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

valores_comuns = conjunto1.intersection(conjunto2)
print("Valores comuns às duas listas:", valores_comuns)

valores_apenas_na_primeira = conjunto1.difference(conjunto2)
print("Valores que só existem na primeira lista:", valores_apenas_na_primeira)

valores_apenas_na_segunda = conjunto2.difference(conjunto1)
print("Valores que só existem na segunda lista:", valores_apenas_na_segunda)

elementos_unicos = conjunto1.union(conjunto2)
print("Elementos não repetidos das duas listas:", elementos_unicos)


primeira_sem_repetidos_na_segunda = conjunto1.difference(conjunto2)
print("A primeira lista sem os elementos repetidos na segunda:", primeira_sem_repetidos_na_segunda)
