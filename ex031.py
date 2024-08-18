distancia = float(input('Escreva a distância da sua viagem: '))
#if distancia <= 200:
   # print('Sua passagem custa R$ {:.2f}'.format(distancia * 0.50))
#else:
   # print('Por sua viagem ser mais longa, ela custa R${:.2f}'.format(distancia * 0.45))
   #outra forma de escrever
preço = float(input('Sua passagem custa R${:.2f}'.format(distancia * 0.50) if distancia <= 200 else 'Por sua viagem ser mais longa, ela custa R${:.2f}'.format(distancia * 0.45)))
