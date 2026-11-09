salario = float(input('Digite o seu salario: '))
aumento = float(input('Digite o aumento em porcento: '))
print('O seu salario era de R${:.2f}, com o aumento de {:.2f} porcento, o seu novo salario é de R${:.2f}' .format(salario, aumento, salario + (salario * aumento / 100)))