soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  # acumulador
        cont += 1  # contador
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
