print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$ '))
print('''Forma de pagamento:
[1] à vista dinheiro / cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4]3x ou mais no cartão  ''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10/100)
    print('Você terá 10% de desconto na sua compra de R${:.2f} e pagará R${:.2f}'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Você terá 5% de desconto na sua compra de R${:.2f} e pagará R${:.2f}'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}. SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (20/100 * preco)
    totparc = int(input('Quantas parcelas? '))
    parcelas = total/totparc
    print('Sua compra será parcelada em {}x de R${:.2f}. COM JUROS'.format(totparc, parcelas))
else:
    total = preco
    print('\033[31mOPÇÃO INVÁLIDA de pagamento.\033[mTente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
