import random
import time
print('>>>>>>>>>>>>>>>>\033[31mJOKENPÔ\033[m<<<<<<<<<<<<<<<<<<')
escolha = str(input(('\033[37mPEDRA\033[m, \033[34mPAPEL\033[m OU \033[33mTESOURA\033[m? '))).lower()
print('PROCESSANDO...')
time.sleep(3)
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
lista = [pedra, papel, tesoura]
aleatorio = random.choice(lista)
if escolha == tesoura and aleatorio == tesoura:
    print(' Tesoura e Tesoura. \033[31mEMPATE\033[m')
elif escolha == tesoura and aleatorio == papel:
    print('Tesoura corta papel. \033[31mVOCÊ GANHOU!!!\033[m')
elif escolha == tesoura and aleatorio == pedra:
    print('Pedra quebra tesoura. \033[31mVOCÊ PERDEU!!!\033[m')
elif escolha == papel and aleatorio == papel:
    print('\033[31mEMPATE\033[m')
elif escolha == papel and aleatorio == tesoura:
    print('Tesoura corta papel. \033[31mVOCÊ PERDEU!!!\033[m')
elif escolha == papel and aleatorio == pedra:
    print('Papel embrulha pedra. \033[31mVOCÊ VENCEU!!!\033[m')
elif escolha == pedra and aleatorio == pedra:
    print('Pedra e Pedra. \033[31mEMPATE\033[m')
elif escolha == pedra and aleatorio == papel:
    print('Papel embrulha pedra. \033[31mVOCÊ PERDEU!!!\033[m')
elif escolha == pedra and aleatorio == tesoura:
    print('Pedra quebra tesoura. \033[31mVOCÊ VENCEU!!!\033[m')
