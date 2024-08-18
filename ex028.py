from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('>>>>>>JOGO DA ESCOLHA<<<<<<')
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS, VOCÊ CONSEGUIU ME VENCER !!!')
else:
    print('VOCÊ PERDEU!!! O número escolhido foi {} e não {}'.format(computador, jogador))
