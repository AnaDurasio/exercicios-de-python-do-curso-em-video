from math import sqrt
co = float(input('Digite o valor o cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = sqrt(co * co + ca * ca)
print('O comprimento da hipotenusa vale {:.2f}'.format(h))