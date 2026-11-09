import math
cateto_oposto = float(input('digite o valor do cateto oposto: '))
cateto_adjacente = float(input('digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))
print('O valor do angulo é: {:.2f}'.format(math.degrees(math.acos(cateto_oposto/hipotenusa))))