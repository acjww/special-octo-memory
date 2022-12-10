# Programa desenvolvido por Amilton Júnior no curso de Desenvolvimento de Sistemas da instituição SENAI
# Esse programa mostra o valor e quantidade de calorias a partir de uma escolha do cliente


# importação da biblioteca os:
import os

nome = str
valor2 = float
valor3 = float
valor4 = float


# Função que será responsável por dividir as seções entre o menu
def writeline():
    print("_____________________________________________________")


# Função que será responsável por dividir valores e calorias
def smallline():
    print("__________________________________")


# Loop caso o cliente queira realizar mais pedidos
resposta2 = 1
while resposta2 == 1:
    os.system("cls")  # Limpar screen do console

    # CARDÁPIO:
    print("Olá, seja bem-vindo(a) ao Restaurante do Programador! \nSegue abaixo o nosso menu:\n")
    print(" 1 - Prato:\n\n  Vegetariano       180Kcal - R$ 8,50\n  Peixe             230Kcal - R$ 12,30\n  "
          "Frango            250Kcal - R$ 7,50\n  Carne             350Kcal - R$ 10,50\n")
    print(" 2 - Sobremesa:\n\n  Abacaxi            75Kcal - R$ 1,50\n  Sorvete diet      110Kcal - R$ 3,50\n  "
          "Mousse diet       170Kcal - R$ 3,00\n  Mousse chocolate  200Kcal - R$ 2,50\n")
    print(" 3 - Bebida:\n\n  Chá               20Kcal - R$ 1,00\n  Suco de laranja   70Kcal - R$ 2,50\n  Suco de Melão"
          "    100Kcal - R$ 3,00\n  Refri diet        65Kcal - R$ 2,00\n")

    resposta = int(input("Para fazer seu pedido DIGITE 1, para sair DIGITE 2: "))

    while resposta > 2 or resposta < 1:  # Tratemento de exeções
        print("Resposta inválida")
        resposta = int(input("Para fazer seu pedido DIGITE 1, para sair DIGITE 2: "))

    if resposta == 1:  # CASO O USUÁRIO QUEIRA FAZER PEDIDOS
        nome = str(input("Qual o seu nome? "))

    elif resposta == 2:  # Caso o usuário não queira fazer pedidos
        print("\n---------- ❥ Volte sempre, estaremos esperando por você! ❥ ----------\n")

    os.system("cls")  # Limpar screen do console

    # Pedido sendo feito
    print("\n-----------------Pedido de ", nome, "-----------------\n")
    print("~>Escolha uma opção de prato de 1 a 4: ")  # Escolha do prato
    print("Caso não queira nenhuma das opções digite 0!\n\n")
    print("  1 - Vegetariano       180Kcal - R$ 8,50\n  2 - Peixe             230Kcal - R$ 12,30\n  3 - Frango"
          "            250Kcal - R$ 7,50\n  4 - Carne             350Kcal - R$ 10,50\n\n")
    prato = int(input("  Qual prato deseja pedir? "))
    writeline()

    while prato > 4:  # Tratemento de exeções
        print("Pedido inválido!")
        prato = int(input("  Qual prato deseja pedir? "))

    print("\n~>Escolha uma opção de sobremesa de 1 a 4: ")  # Escolha da sobremesa
    print("Caso não queira nenhuma das opções digite 0!\n\n")
    print("  1 - Abacaxi            75Kcal - R$ 1,50\n  2 - Sorvete diet      110Kcal - R$ 3,50\n  3 - Mousse diet"
          "       170Kcal - R$ 3,00\n  4 - Mousse chocolate  200Kcal - R$ 2,50\n\n")
    sobremesa = int(input("  Qual sobremesa deseja pedir? "))
    writeline()

    while sobremesa > 4:  # Tratemento de exeções
        print("Pedido inválido!")
        sobremesa = int(input("  Qual sobremesa deseja pedir? "))

    print("\n~>Escolha uma opção de bebida de 1 a 4: ")  # Escolha da bebida
    print("Caso não queira nenhuma das opções digite 0!\n\n")
    print("  1 - Chá               20Kcal - R$ 1,00\n  2 - Suco de laranja   70Kcal - R$ 2,50\n  3 - Suco de Melão    "
          "100Kcal - R$ 3,00\n  4 - Refri diet        65Kcal - R$ 2,00\n\n")
    bebida = int(input("  Qual bebida deseja pedir? "))
    writeline()

    while bebida > 4:  # Tratemento de exeções
        print("Pedido inválido!")
        bebida = int(input("  Qual bebida deseja pedir? "))

    # Definindo pratos a partir da escolha do cliente:
    if prato == 1:
        print("\n Seu pedido foi:   \n   - Prato: Vegetariano")
    elif prato == 2:
        print("\n Seu pedido foi:   \n   - Prato: Peixe")
    elif prato == 3:
        print("\n Seu pedido foi:   \n   - Prato: Frango")
    elif prato == 4:
        print("\n Seu pedido foi:   \n   - Prato: Carne")

    # Atribuindo valores aos pratos:
    if prato == 1:
        calorias = 180
        valor = 8.50
        prato = calorias
        valor2 = valor

    elif prato == 2:
        calorias = 230
        prato = 230
        valor = 12.30
        valor2 = valor

    elif prato == 3:
        calorias = 250
        prato = 250
        valor = 7.50
        valor2 = valor

    elif prato == 4:
        calorias = 350
        prato = 350
        valor = 10.50
        valor2 = valor

    # Definindo sobremesa a partir da escolha do cliente:
    if sobremesa == 1:
        print("   - Sobremesa: Abacaxi")
    elif sobremesa == 2:
        print("   - Sobremesa: Sorvete Diet")
    elif sobremesa == 3:
        print("   - Sobremesa: Mousse Diet")
    elif sobremesa == 4:
        print("   - Sobremesa: Mousse Chocolate ")

    # Atribuindo valores às sobremesas:
    if sobremesa == 1:
        calorias = 75
        sobremesa = 75
        valor = 1.50
        valor3 = valor
    elif sobremesa == 2:
        calorias = 110
        sobremesa = 110
        valor = 3.50
        valor3 = valor
    elif sobremesa == 3:
        calorias = 170
        sobremesa = 170
        valor = 3.00
        valor3 = valor
    elif sobremesa == 4:
        calorias = 200
        sobremesa = 200
        valor = 2.50
        valor3 = valor

    # Definindo bebidas a partir da escolha do cliente:
    if bebida == 1:
        print("   - Bebida: Chá")
    elif bebida == 2:
        print("   - Bebida: Suco de Laranja")
    elif bebida == 3:
        print("   - Bebida: Suco de Melão")
    elif bebida == 4:
        print("   - Bebida: Refri Diet")
    smallline()

    # Atribuindo vaores às bebidas:
    if bebida == 1:
        calorias = 20
        bebida = 20
        valor = 1.00
        valor4 = valor
    elif bebida == 2:
        calorias = 70
        bebida = 70
        valor = 2.50
        valor4 = valor
    elif bebida == 3:
        calorias = 100
        bebida = 100
        valor = 3.00
        valor4 = valor
    elif bebida == 4:
        calorias = 65
        bebida = 65
        valor = 2.00
        valor4 = valor

    # Soma das calorias:
    soma = prato + bebida + sobremesa

    print("\n   Total de calorias: \n", "       ", soma, "Kcal")
    smallline()

    # Soma dos valores:
    soma2 = valor2 + valor3 + valor4
    print("\n   Valor total: \n", "       R$", soma2)
    smallline()

    resposta2 = int(input("\nPara fazer mais um pedido DIGITE 1, para finalizar DIGITE 2: "))

    while resposta2 > 2 or resposta2 < 1:  # Tratemento de exeções
        print("\nResposta inválida!")
        resposta2 = int(input("\nPara fazer mais um pedido DIGITE 1, para finalizar DIGITE 2: "))

    if resposta2 == 2:  # Caso o cliente não queira realizar mais pedidos
        print("\nSeu pedido está sendo preparado! \nObrigado pela preferência! :)")
