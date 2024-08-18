km = float(input('Quantos quilômetros foram percorridos?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
pago = (dias * 60) + (0.15 * km)
print(' Como você alugou o carro por {} dias, terá que pagar R${:.2f} .'.format(dias, pago))