menu = """
        [D] Depositar
        [S] Sacar
        [E] Extrato
        [Q] Sair

==>"""

saldo = 0
LIMITE = 500
LIMITE_SAQUES = 3
numero_saques = 0
extrato = " "


while True:
    opcao = input(menu)

    if opcao.upper() == 'D':
        print("Depósito:")
        valor = float(input("valor do depósito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor R$ {valor: .2f} \n"

    elif opcao.upper() == "S":
        print("Saque:")
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("valor do saque:"))
            if valor <= LIMITE:
                if valor <= saldo:
                    saldo -= valor
                    extrato += f"Saque no valor R$ {valor: .2f}\n"
                else:
                    print("Saldo insuficiente para saque.")
        else:
            print("Excedeu o limite de saque diário.")
        numero_saques += 1


    elif opcao.upper() == "E":
        print("Extrato:")
        print(extrato)
        print()
        print(f"Seu Saldo atual é: {saldo: .2f}")

    elif opcao.upper() == "Q":
        break
    else:
        print("Opção inválida, por favor tente novamente...")
    

