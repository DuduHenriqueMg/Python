numero = int(input("Insira um número de cinco dígitos: "))
           
string = str(numero)

if len(string) != 5:
    print("Por favor, insira um número de cinco dígitos.")
else:
    for i in string:
        print(i, end="   ")
