expressao = input("Digite a expressão com parênteses: ")
pilha = []
for c in expressao:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if not pilha:
            print("Erro")
            break
        else:
            pilha.pop()
    else:
        if pilha:
            print("Erro: Há parênteses abertos que não foram fechados.")
        else:
            print("Os parênteses estão certos")