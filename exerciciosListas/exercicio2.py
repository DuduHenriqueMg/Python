palavra = "teste"
letras_corretas = []
tentativas = 6

print("Bem-vindo ao Jogo da Forca!")

while True:
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

    if all(letra in letras_corretas for letra in palavra):
        print("Parabéns! Você ganhou!")
        break

    if tentativas == 0:
        print("Você perdeu! A palavra correta era:", palavra)
        break

    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        letras_corretas.append(letra)
        print("Letra correta!")
    else:
        print("Letra incorreta!")
        tentativas -= 1


