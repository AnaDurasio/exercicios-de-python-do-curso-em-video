velocidade = float(input('Qual é a velocidade atual do seu carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('MULTADO! Por exceder o limite permitido de 80km/h, você deve pagar uma multa de R$ {:.2f}!'.format(multa))

print('Tenha um bom dia! Dirija com segurança!') #CONDIÇÃO SIMPLES, SEM O USO DO ELSE
