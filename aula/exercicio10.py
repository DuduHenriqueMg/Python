num = int(input("Digite o numero:"))

aux=num
count=0

while aux>0:
    
    if num%aux==0:
        count+=1
    aux -=1

if count==2:
    print(f"O numero {num} é primo")
else:
    print(f"O numero {num} não é primo")
    
