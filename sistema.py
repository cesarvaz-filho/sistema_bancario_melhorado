def menu():
    menu = """
    ############ MENU ############
    Digite uma opção

    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [n] = Nova conta
    [u] = Novo usuário
    [q] = Sair
    ==>"""
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} com sucesso")
    else:
        print("Valor inválido")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = valor >= limite

    if excedeu_saldo:
        print("\nSem saldo suficiente")
    elif excedeu_limite:
        print("\nSem limite suficiente")
    elif excedeu_saque:
        print("\nLimite de saque atingido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque com sucesso")
    else:
        print("Valor inválido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n###########Extrato###########")
    print("Não foram realizadas movimentações" if not extrato else extrato) 
    print(f"Saldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(apenas números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("CPF já existente")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("informa da data de nascimento(dd-mm-aaaa): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})
    print("Usuário criado!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não localizado.")

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUE
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "u":
            criar_usuario(usuarios)
        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "q":
            break
        else:
            print("Operação inválida. por favor selecione novamente")


main()
