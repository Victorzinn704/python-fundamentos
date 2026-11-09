from time import sleep
distancia = int(input('Qual a distância da viagem em Km? '))
print('Calculando o preço da passagem...')
sleep(2)  # Simula um atraso no cálculo
print('a distancia da viagem é de {}Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da passagem é R${:.2f}'.format(preco))
print('Tenha uma boa viagem!')