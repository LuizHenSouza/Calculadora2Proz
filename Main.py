# Faça uma função calculadora que os números e as operações serão feitas pelo usuário.
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
# No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro,
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada.
# Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”,
# o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.

import operacoes, menu, time
while(10 > 7):
    op, v1, v2 = menu.Menu()

    if(op == 0):
        break
    if(op > 5 or op < 0):
        continue

    if(op == 1):
        print("O resultado da operação entre ", str(v1), " e ", str(v2), " é igual a: " + str(operacoes.Sum(v1,v2)))
        time.sleep(5)
    elif(op == 2):
        print("O resultado da operação entre ", str(v1), " e ", str(v2), " é igual a: " + str(operacoes.Sub(v1,v2)))
        time.sleep(5)
    elif(op == 3):
        print("O resultado da operação entre ", str(v1), " e ", str(v2), " é igual a: " + str(operacoes.Mult(v1,v2)))
        time.sleep(5)
    elif(op == 4):
        print("O resultado da operação entre ", str(v1), " e ", str(v2), " é igual a: " + str(operacoes.Div(v1,v2)))
        time.sleep(5)

SystemExit()

# Tá gambiarrado kkkkkk Não tenho muito costume com python, mas, conserto assim que puder