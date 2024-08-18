n1 = float(input('\033[7;97mEscreva sua primeira nota: \033[m'))
n2 = float(input('\033[7;97mEscreva sua segunda nota: \033[m'))
m = (n1+n2)/2
print('Sua média é {:.2f}'.format(m))
if m < 5:
    print('Você está \033[31mREPROVADO')
elif 5 <= m <= 6.9:
    print('Você está de \033[33mRECUPERAÇÃO')
elif m >= 7.0:
    print('Você está \033[34mAPROVADO')


