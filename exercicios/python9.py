r = float(input('Quanto voce tem na carteira? R$'))
USD = r / 5.20
EUR = r / 5.70
BTC = r / 100000.00
moeda = str(input('Qual moeda voce quer converter? (USD, EUR, BTC)')).upper()

if moeda == 'USD':
    print('Voce pode comprar {:.2F} dolares com {} reais'.format(USD, r))
elif moeda == 'EUR':
    print('Voce pode comprar {:.2F} euros com {} reais'.format(EUR, r))
elif moeda == 'BTC':
    print('Voce pode comprar {:.2F} bitcoins com {} reais'.format(BTC, r))
else:
    print('Moeda invalida')