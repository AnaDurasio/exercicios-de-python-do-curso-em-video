import math
angulo = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O ângulo {} tem: \n seno = {:.2f} \n cosseno = {:.2f} \n tangente = {:.2f}'.format(angulo, sen, cos, tang))
