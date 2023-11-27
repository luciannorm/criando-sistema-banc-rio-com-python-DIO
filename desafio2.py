def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar conta
    [q] Sair
    
    => """
    return input(menu)

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato

def sacar(*,valor,saldo,extrato,limite,numero_saques,LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo,extrato

def visualizar_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF, apenas números: ")
    usuario = filtra_usuario(cpf,usuarios)

    if usuario:
        print("Já existe esse usuário cadastrado...")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa:")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf ,"endereco": endereco})
    print("usuário criado com SUCESSO!!!")

def filtra_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Informe o CPF, apenas números: ")
    usuario = filtra_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso!!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado")

def listar_clientes():
    global clientes
    for chave, valor in clientes.items():
        print(chave,valor)

def listar_contas(contas):
    for conta in contas:
        linha = f"""
                Agência: {conta["agencia"]}
                Cc: {conta["numero_conta"]}
                Titular: {conta["usuario"]["nome"]}
        """
        print(linha)

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    agencia= '0001'
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo,extrato = depositar(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo,extrato = sacar(
                valor=valor,
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,)

        elif opcao == "e":
            visualizar_extrato(saldo,extrato=extrato)

        elif opcao == "q":
            break

        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia,numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()

