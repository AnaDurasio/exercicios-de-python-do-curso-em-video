from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Para realizar uma operação com esses dois números escolha:  
    [1] SOMAR       
    [2] PARA MULTIPLICAR
    [3] PARA SABER O MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>>>>Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado entre {} x {} é igual a {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é {} '.format(n1, n2, maior))
        elif n1 == n2:
            print('0s dois valores são iguais')
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior valor é {} '.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os novos números:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')






