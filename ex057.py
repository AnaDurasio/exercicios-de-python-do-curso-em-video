
genero = str(input('Informe seu gênero: [M/F] ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Dados inválidos.Por favor, informe seu gênero: ')).strip().upper()[0]
print('Gênero {} registrado com sucesso'.format(genero))
