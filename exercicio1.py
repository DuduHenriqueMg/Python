
num1 = int(input("Insira o primeiro inteiro: "))
num2 = int(input("Insira o segundo inteiro: "))
    
soma = num1 + num2
produto = num1 * num2
diferenca = num1 - num2
    
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Indefinida (divisão por zero)"

print("Soma:", soma)
print("Produto:", produto)
print("Diferença:", diferenca)
print("Divisão:", divisao)
