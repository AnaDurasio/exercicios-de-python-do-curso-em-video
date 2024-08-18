real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = float(real / 3.27)
print('Com R${:.2f} reais você pode comprar US${:.2f} doláres'.format(real, dolar))