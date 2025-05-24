menu= '''
 Bem vindo a sua conta!
_________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

_________________________

Sua resposta ->  '''

saldo= 0
limite= 500
extrato= ""
numero_saques= 0
limite_saque= 3
resposta= ""

while True:
    opcao= input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(extrato)
        
        else:
            print("O valor inserido não é válido.")
    
            

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saque

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
            print(extrato)

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "3":
        print("\n_____________EXTRATO_____________")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("________________________________")

    elif opcao == "4":
        print('''______ Obrigado por usar nossos serviços, Volte sempre! ______''')
        break 

    else:
        print("Operação inválida, tente novamente.")  