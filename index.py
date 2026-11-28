import json

print("---- SISTEMA BANCÁRIO ----")
print("Selecione a opção que deseja visualizar: ")



banco_infos = []

def gravar_infos():
    while True:
        print("\n[1] Criar conta.\n[2] Depositar. \n[3] Extrato. \n[4] Sacar. \n[5] Sair.")

        op = int(input("Escolha:"))

        if op == 1:
            print("\nConta: ")
            conta = {}
            conta ['Nome'] = input("Nome:")
            conta ['Senha'] = input("Senha:")
            conta ['Agência'] = input("Agência:")
            conta ['Conta'] = input("Conta:")
            conta ['CPF/CPNJ'] = input("CPF/CPNJ:")
            conta ['CEP'] = input("CEP:")
            conta ['Saldo:'] = 0
            conta ['Extrato'] = []
                      
            gravar_infos.append(conta)
            print("\nConta Registrada com sucesso!")


        elif op == 2:
            print("\nRealizar depósito: ")
            conta ['Agência'] = input("Agência")
            conta ['Conta'] = input("Conta:")
            conta ['Senha'] = input("Senha:")

            gravar_infos.append(conta)
            print("\nConta Registrada com sucesso!")


        elif op == 3:
            print("\nVer extrato: ")
            conta ['Agência'] = input("Agência:")
            conta ['Conta'] = input("Conta:")
            conta ['Valor'] = input("Valor:")

            gravar_infos.append(conta)
            print("\nConta Registrada com sucesso!")


        elif op == 4:
            print("\nRealizar saque:")
            conta ['Agência'] = input("Agência")
            conta ['Conta'] = input("Conta:")
            conta ['Senha'] = input("Senha:")
            conta ['Valor'] = input("Valor:")
            conta ['Saldo'] = print()


            gravar_infos.append(conta)
            print("\nSaque Realizado com sucesso!")
        



            
        

gravar_infos();