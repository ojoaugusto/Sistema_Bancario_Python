menu = """
-------------- Escolha uma opção --------------
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

-----------------------------------------------
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        print("Deposito")
        valor_deposito = float(input("qual o valor do deposito? \n"))
        if valor_deposito > 0:
            print("deposito aceito!")
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
        else:
            print("FALHOU! valor informado inválido")

    elif opcao.lower() == "s":
                
        if numero_saques <= LIMITE_SAQUES-1:
            print("Saque")
            valor_saque = float(input("qual o valor do saque? \n"))
            
            if valor_saque > saldo:
                print("Saldo insuficiente")
            elif valor_saque <= limite:
                print("Saque realizado com sucesso!")
                extrato += f"Saque: R${valor_saque:.2f}\n"
                saldo -= valor_saque
                numero_saques += 1
            else:
                print("valor de saque muito alto")
        
        else:
            print("número de saques atingidos")

                    
    
    elif opcao.lower() == "e":
        print("-------------- Extrato --------------")
        print(extrato)        
        
        print(f" Seu saldo é de R${saldo} ")

    elif opcao.lower() == "q":
        print("Saindo")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada: ")


