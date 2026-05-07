from Conta import Cliente,Conta, ContaCorrente, ContaPoupanca
lista_usuario = []
def cadastrar_cliente(nome, cpf, lista):  
    novo_cliente = Cliente(nome, cpf)
    lista.append(novo_cliente)
    print(f"Usuário {nome} cadastrado com sucesso!")





def menu():
    while True:
        print("┌──────────────────────────────────────┐")
        print("|                                      |")
        print("│         🌟 MENU PRINCIPAL 🌟        │")
        print("|                                      |")
        print("├──────────────────────────────────────┤")
        print("|  [ 1 ]  👤 Adicionar Cliente         |")
        print("│  [ 2 ]  🤖 Ver Saldo                 │")
        print("│  [ 3 ]  🐦‍🔥 Depositar                 │")
        print("│  [ 4 ]  👾 Sacar                     │")
        print("│  [ 5 ]  🌀 Sair                      │")
        print("|                                      |")
        print("└──────────────────────────────────────┘")

        opcao = input("    Escolha uma opção:    ")

        match opcao:
            case "1":
                nome = input("Digite seu nome: ")
                cpf = input("Digite seu CPF: ")

                cadastrar_cliente(nome,cpf, lista_usuario)
                
            case "2":
                resposta = input("Usuario que deseja ver o saldo: ")
                        
            case "3":
                pass
            case "4":
                pass
            case "5":
                break


print(menu())
