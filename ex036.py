valor = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
pm = valor / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valor, anos, pm))
exececao = salario * 30/100
print('Comparando tem que pagar {} e o mínimo é de {}'.format(pm, exececao))
if pm <= exececao:
    print('EMPRÉSTIMO \033[34mCONCEDIDO\033[m!. Você pagará R$ {:.2f} por mês'.format(pm))
else:
    print('EMPRÉSTIMO \033[31mNEGADO\033[m!')