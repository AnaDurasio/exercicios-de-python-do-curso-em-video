p1 = float(input('Primeira reta: '))
p2 = float(input('Segunda reta: '))
p3 = float(input('Terceira reta: '))
if p1 < (p2+p3) and p2 < (p1+p3) and p3 < (p1+p2):
    print('Essas retas PODEM formar um triângulo.')
    if p1 == p2 == p3:
        print('Esse triângulo será do tipo equilátero, pois todos os seus lados são iguais.')
    if p1 == p2 or p2 == p3 or p3 == p1:
        print('Esse triãngulo é do tipo isósceles, pois 2 de seus lados são iguais.')
    if p1 != p2 != p3 != p1:
        print('Esse triângulo é do tipo escaleno, pois todos os seus lados são diferentes.')
else:
    print('Essas retas NÃO PODEM formar um triângulo.')

