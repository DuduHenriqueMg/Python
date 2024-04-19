agenda = {}
campos = ["nome", "telefone", "email," "datanasc"]

while True:
    
    ope = int(input(""" 
                        Agenda Pessoal
                        
                        1 - Salvar Contato
                        2 - Alterar Contato
                        3 - Buscar Contato
                        4 - Apagar Contato
                        5 - Listar Contatos
                    
                    
                pressione 0 para sair.
                    
                    
    """))
    
    if ope == 0:
        break;
    elif ope == 1:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        datanasc = input("Data de nascimento: ")
        contato = [nome, telefone, email, datanasc]
        agenda[nome] = contato
        print("Contato salvo");
        
    elif ope == 2:
        nome = input("Insira o nome do contato: ")
        dado = input("Qual dado quer alterar: ")
        novo = input("Qual novo valor: ")
        agenda[nome][campos.index(dado)] = novo
        print("O campo foi alterado")
    elif ope == 3:
        nome = input("Insira o nome do contato: ")
        contato = agenda[nome]
        print(contato)

    elif ope == 4:
        nome = input("Insira o nome do contato: ");
        del agenda[nome];
    
    elif ope == 5:
        for contato in agenda.values():
            print(contato)
            
    else: 
        print("Opção invalida")