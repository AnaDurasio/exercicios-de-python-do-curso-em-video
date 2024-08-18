from datetime import date
atual = date.today().year
ano = int(input('Qual o seu ano de nascimento? '))
genero = str(input('''Qual o seu gênero? \033[34m
Digite:
 [1] para feminino
 [2] para masculino\033[m. '''))
if genero == '1':
    print('\033[31mVocê não precisa fazer alistamento militar obrigatório.\033[m')
elif genero == '2':
    print('Será que você já está na idade de alistamento?')
idade = atual - ano
print('Quem nasceu em {} tem {} anos no ano de {}.'.format(ano, idade, atual))
if genero == 2 and idade == 18:
    print('Já é hora de você se alistar ao serviço militar!')
elif genero == 2 and idade < 18:
    saldo = 18 - idade
    print('Você ainda vai se alistar. Ainda faltam {} anos para o seu alistamento.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano))
    ano = atual + saldo
elif genero == 2 and idade > 18:
    saldo = idade - 18
    print('Seu tempo de alistamento já passou! Você deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(ano+18))
    ano = atual - saldo

