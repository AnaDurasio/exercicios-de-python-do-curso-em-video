cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade.capitalize()[:5] == 'Santo')
#outra forma de escrever
print(cidade[:5].upper() == 'SANTO')
print(cidade[:5].lower() == 'santo')