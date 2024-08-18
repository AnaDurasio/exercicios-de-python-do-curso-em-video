import random
p1 = '\033[4;31mAlison Dilaurentis\033[m'
p2 = '\033[4;34mSpencer Hastings\033[m'
p3 = '\033[4;37mHanna Marin\033[m'
p4 = '\033[4;33mAria Montgomery\033[m'
p5 = '\033[4;36mEmily Fields\033[m'
p6 = '\033[4;97mMona Vanderwaal\033[m'
p7 = '\033[4;35mJenna Marshall\033[m'
lista = [p1, p2, p3, p4, p5, p6, p7]
escolhida = random.choice(lista)
print('{}<<<<<<<<<< PLL GAME >>>>>>>>>>{}'.format('\033[31;107m', '\033[m'))
melhor = str(input('{} Qual a melhor personagem de Pretty Little Liars? {}'.format('\033[30;107m', '\033[m'))).title().strip()
if melhor == escolhida:
    print('VOCÊ ACERTOU!!! A melhor personagem de PLL é a {}!'.format(escolhida))
else:
    print('VOCÊ ERROU!! A melhor personagem de PLL é a {}!'.format(escolhida))
