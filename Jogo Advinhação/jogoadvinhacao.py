"Desenvolvido por Flávia"

from random import randint
print('''=============================================================================================
         \n         Olá usuário, eu sou o computador, e quero interagir um pouco com você!!

         Dica: Vou pensar num número de 0,10, topa advinhar??? \n
=============================================================================================''')

computador = randint(0,10)
cont = 0
usuario = int(input("\nDigite o número, usuário: "))

while True:
    if usuario == computador:
        print("ACERTOU!!!!!")
        cont+= 1
        break
    else:
        while True:
            if usuario != computador:
                print("QUAAAAASE!\n")
                usuario = int(input("Digite o número, usuário: "))
                if usuario == computador:
                    cont += 1
                    break
            cont += 1

print('''=========================================================================================''')
print("\nEu pensei no número {} também.".format(computador))
print("\nVocê acertou com {} tentativas!".format(cont))
print('''=========================================================================================''')