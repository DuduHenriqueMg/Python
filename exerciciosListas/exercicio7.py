grid = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']];

for linha in grid:
    for coluna in linha:
        print(coluna, end=" ");
    print("");
    
venceu = False;
velha = False;
tentativas = 0;
    
while not venceu and not velha:        
    jogada = input("Coloque X ou O: ");
    i = int(input("Em qual linha: " ));
    j = int(input("Em qual coluna: " ));

    grid[i][j] = jogada;
    tentativas += 1;
    
    for linha in grid:
        for coluna in linha:
            print(coluna, end=" ");
        print("");
        
    if (grid[0][0] == grid [1][1] == grid[2][2]):
        venceu = True;
        break;
    elif (grid[0][2] == grid [1][1] == grid[2][2]):
        venceu = True;
        break;
    else:
        for i in range(0, len(grid)):
            if(grid[i][0] == grid[i][1]==grid[i][2]):
                venceu = True
                break;
            elif(grid[0][i] == grid[1][i]==grid[2][i]):
                venceu = True
                break;

    if tentativas == 9:
        velha = True ;  
        
if venceu == True:
    print(f"O jogador do {jogada} Ganhou");
else:
    print("Perdeu");
    