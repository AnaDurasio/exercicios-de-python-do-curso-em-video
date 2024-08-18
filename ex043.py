peso = float(input('Escreva seu peso: (Kg) '))
altura = float(input('Escreva o seu altura: (m) '))
imc = (peso / (altura ** 2))
print('Seu imc é igual a {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')

