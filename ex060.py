n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x' if c > 1 else ' = ', end=' ')
    f *= c   #fatorial recebe fatorial vezes c
    c -= 1 #c recebe c menos 1
print('{}'.format(f))
