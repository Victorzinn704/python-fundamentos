L = float(input('Qual a largura da parede em metros? '))
A = float(input('Qual a altura da parede em metros? '))
area = L * A
tinta = area / 2
print('A area da parede é de {:.2F} m² e a quantidade de tinta necessária para pintar a parede é de {:.2F} litros'.format(area, tinta))