carro = int(input('qual a velocidade do carro?'))
if carro >80:
    print('Multado! Você passou a {}Km/h, excedeu o limite de velocidade que é de 80Km/h'.format(carro))
multa = (carro - 80) * 7
print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
