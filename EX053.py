frase = str(input('Digite uma frase: ')).strip().upper()
print('Você digitou a frase {}'.format(frase))
palavras = frase.split()
junto = ''.join(palavras) #eliminei os espaços do meio
inverso = ''
'''inverso = junto[::-1] ''' #fazendo sem o for
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
