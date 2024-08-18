import random
a1 = 'RED'
a2 = 'FEARLESS'
a3 = 'SPEAK NOW'
a4 = 'TAYLOR SWIFT'
a5 = 'MIDNIGHTS'
a6 = 'REPUTATION'
a7 = 'FOLKLORE'
a8 = 'EVERMORE'
a9 = 'LOVER'
a10 = '1989'
lista = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
escolhido = random.choice(lista)
print('<<<<<<<<<SWIFTIE GAME>>>>>>>>>>>>>>>')
melhor = str(input('Qual é o melhor álbum da Taylor segundo o computador? ')).upper()
if melhor == escolhido:
    print('ACERTOU!! O melhor álbum da Taylor é o {}'.format(escolhido))
else:
    print('ERROU!! O melhor álbum da Taylor é o {}'.format(escolhido))
pior = str(input('Qual é o pior álbum da Taylor de acordo com o computador? ')).upper()
pescolhido = random.choice(lista)
if pior == pescolhido:
    print('ACERTOU!! O pior álbum da Taylor é o {}'.format(pescolhido))
else:
    print('ERROU!! O pior álbum da Taylor é o {}'.format(pescolhido))
