n = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n > n2:
    print('O primeiro, que é o valor {}, é maior'.format(n))
elif n < n2:
    print('O segundo, que é o valor {}, é maior'.format(n2))
else:
    print('Não existe valor maior, os valores {} e {} são iguais'.format(n, n2))
