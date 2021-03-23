"Desenvolvido por Flávia"


from random import randint
from time import sleep


print('''Suas opções:
         [0] PEDRA
         [1] PAPEL
         [2] TESOURA ''')

print("\n")

opcoes = ('Pedra', 'Papel', 'Tesoura') #opções do jogo, para poder aparecer lá no print do que jogaram

op_jogador = int(input("Digite sua opção: "))

while True:
    if op_jogador != 0 and op_jogador != 1 and op_jogador != 2:
        print("Jogada invalida, tente novamente")

        op_jogador = int(input("Digite sua opção: "))

    else:
        break
    
    
#esse sleep serve para demorar um tempo para postar a proxima linha

print("\n")

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

computador = randint(0,2)             #para o computador escolher aleatorio 

#mostrar opções 
print("\n")
print("O computador escolheu {}".format(opcoes[computador]))
print("Você escolheu {}".format(opcoes[op_jogador]))
print("\n")

#saber quem venceu:

if (op_jogador == 0 and computador == 0) or (op_jogador == 1 and computador == 1) or (op_jogador == 2 and computador == 2):
    print("Ihhh, deu empate!!!!!!")

elif (op_jogador == 2 and computador == 1) or (op_jogador == 1 and computador == 0) or (op_jogador == 0 and computador == 2):
    print("Você ganhou!!!!!!")
    
else:
    print("Computador Venceu!!!!!!")