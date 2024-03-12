import os, time
def Menu():
    os.system('Cls')
    print("Escolha a operação que deseja realizar:")
    print("1-Soma\t2-Subtração\t3-Multiplicação\t4-Divisão\t0-Sair")
    escolha = int(input())
    if(escolha == 0):
        return escolha, 0, 0
    elif(escolha > 0 and escolha < 5):
        operacao = escolha
        valor1 = float(input("Digite o primeiro valor da operação: "))
        valor2 = float(input("Digite o segundo valor da operação: "))
        return operacao, float(valor1), float(valor2)
    else:
        print("Essa opção não existe!")
        time.sleep(3)
        return 9, 9, 9