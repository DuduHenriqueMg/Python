segundos = int(input("Insira a quantidade de segundos: "))

segundos_res = segundos%60
minutos = (segundos//60)%60
horas = ((segundos//60)//60)%24
dia = ((segundos_res//60)//60)//24

print(f"{dia:03d} dias - {horas:02d}:{minutos:02d}:{segundos_res:02d}")
