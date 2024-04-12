salas = [1, 2, 3, 4, 5];
lugares_vagos = [10, 2, 1, 3, 0];

while True:
    sala_solicitada = int(input("Qual sala:"))
    if sala_solicitada == 0:
        break;
    
    qtd_lugares = int(input("Quantos lugares:"))

    

    for i, sala in enumerate(salas):
        if sala_solicitada == sala:
            if qtd_lugares <= lugares_vagos[i]:
                lugares_vagos[i] -= qtd_lugares
                print("Ingressos vendidos")
            else: 
                print("Lugares cheios")
    
    