from datetime import datetime

def exibir_menu():
    menu = ''' 
    Bem-vindo à sua conta!
    _________________________

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

    _________________________

    Sua resposta -> '''
    return input(menu)

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor inserido não é válido.")
    except ValueError:
        print("Valor inválido. Por favor, insira um número válido.")
    return saldo, extrato

def sacar(saldo, limite, extrato, numero_saques, limite_saque):
    data = datetime.now().strftime("%d/%m/%Y")

    try:
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= limite_saque:
            print(f"Operação falhou! Número máximo de saques do dia {data} excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    print("\n_____________EXTRATO_____________")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(f"{extrato}\nRealizado na data: {data}.")
        print(f"\nValor do Saldo: R$ {saldo:.2f}.")
        print("________________________________")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 2

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques, limite_saque)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            print("______ Obrigado por usar nossos serviços, Volte sempre! ______")
            break
        else:
            print("Operação inválida, tente novamente.")

if __name__ == "__main__":
    main()
