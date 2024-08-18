n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} '.format(nome[0]))
# para saber o ultimo nome, preciso pedir o nome que está em o comprimento - 1
print('Seu último nome é {} '.format(nome[len(nome)-1]))
print(len(nome))
print(nome)
