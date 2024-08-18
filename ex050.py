soma = 0
cont = 0
for n in range(1, 7):
    n1 = int(input('Digite o {} valor: '.format(n)))
    if n1 % 2 == 0:
      soma = soma + n1
      cont = cont + 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))


