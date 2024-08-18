#exercicio de p.a
p = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
     print(' {} '.format(c), end='-> ')


