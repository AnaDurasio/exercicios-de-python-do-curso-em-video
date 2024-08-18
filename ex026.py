frase = str(input('Digite uma frase: ')).upper().strip()
# Esse +1 serve para somar um número para a posição de A,
# de forma que a posição seja dada considerando a forma como lemos, sem considerar o zero
print('A letra A aparece {} vezes'.format(frase.count('A')+1))
print('A letra A aparece pela primeira vez em {}'.format(frase.find('A')))
# dessa forma ele vai procurar a partir do lado direito, assim ele vai achar a última vez em que a letra 'A' aparece.
print('A última ocorrência da letra A acontece em {}'.format(frase.rfind('A')+1))
