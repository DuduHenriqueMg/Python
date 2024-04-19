frase = input("Digite uma frase: ")

count = {}

for c in frase:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

print(count)
