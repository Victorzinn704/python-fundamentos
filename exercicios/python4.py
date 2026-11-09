n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
d = n1/n2 
m = n1*n2
di = n1//n2
e = n1**n2
print('As operaçoes entre {} e {} sao:'.format(n1, n2))
print('A soma é: {}'.format(s))
print('A subtração é: {}'.format(n1-n2))
print('A multiplicação é: {}'.format(m))
print('A divisão é: {:.3f}'.format(d))
print('A divisão inteira é: {}'.format(di))
print('A potencia é: {}'.format(e))
