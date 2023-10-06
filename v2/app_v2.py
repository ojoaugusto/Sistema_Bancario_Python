import textwrap

def menu():
    menu = """\n
    -------------- Escolha uma opção -------------- 
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [nc] - Nova conta
    [lc] - Listar contas
    [nu] - Novo usuário
    [q] - Sair

    -----------------------------------------------
    """
    return input(textwrap.dedent(menu))

def depositar(valor, saldo, extrato):
    if valor > 0:
        print("Depósito realizado com sucesso! \n")
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("Valor informado inválido")

    return saldo, extrato


def sacar(valor, saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    if LIMITE_SAQUES < numero_saques:
        
        if valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite:
            print("Valor de saque muito alto!")
        else:
            print("Saque realizado com sucesso!")
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R${valor:.2f}\n"
    else:
        print("Número máximo de saques atingindos!")

    return saldo, extrato, numero_saques



def exibir_extrato(saldo, /, *, extrato):
    print("-------------- Extrato --------------")
    print(extrato)        
        
    print(f" Seu saldo é de R${saldo} ")

def criar_usuario(usuarios):
    cpf = int(input("Digite seu CPF - apenas números: \n"))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Já existe usuário com esse CPF ===")
        return None
            
    nome = str(input("Insira seu nome: \n"))
    data_nascimento = str(input("Digite sua data de nascimento: \n"))
    endereco = str(input("Informe o endereço (logradouro, nº - bairro - Cidade/sigla Estado): \n"))
        
    usuarios.append({"nome": nome, "data_nascimnto": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("usuário cadastrado com sucesso!")
    
    


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF do usuário: \n"))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia,
                "numeor_conta": numero_conta,
                "usuario": usuario
                }
    
    print("Usuário não encontrado!")

def listar_conta(contas):
    for conta in contas:
        linha = f"""
        Agencia: {conta["agencia"]}
        C/c: {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        """

        print("-" * 100)
        print(textwrap.dedent(linha))

def main():
    numero_saques = 0
    LIMITE_SAQUES = 3
    limite = 500
    saldo = 0
    extrato = ""
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao.lower() == "d":
            valor = float(input("Informe o valor do deposito: \n"))

            saldo, extrato = depositar(valor=valor, saldo=saldo, extrato=extrato)
        
        elif opcao.lower() == "s":
            valor = float(input("Informe o valor do saque: \n"))

            saldo, extrato, numero_saques = sacar(
                valor = valor,
                saldo = saldo,
                extrato = extrato,
                numero_saques = numero_saques,
                LIMITE_SAQUES = LIMITE_SAQUES,
                limite= limite
            )

        elif opcao.lower() == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao.lower() == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia= AGENCIA, numero_conta = numero_conta, usuarios = usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao.lower() == "lc":
            listar_conta(contas)

        elif opcao.lower() == "nu":
            criar_usuario(usuarios)

        elif opcao.lower() == "q":
            print("Encerrando acesso")
            break

main()