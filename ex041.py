from datetime import date
ano = int(input('Escreva o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('\033[1;34mCATEGORIA MIRIM')
elif 9 < idade <= 14:
    print('\033[1;31mCATEGORIA INFANTIL')
elif 14 < idade <= 19:
    print('\033[1;33mCATEGORIA JUNIOR')
elif 19 < idade <= 25:
    print('\033[1;36mCATEGORIA SÊNIOR')
else:
    print('\033[1;30mCATEGORIA MASTER')