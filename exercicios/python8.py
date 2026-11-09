n = int(input('digite um numero: '))
print('A tabuada do {} é:'.format(n))
for i in range(0, 11):
    print('{} x {} = {}'.format(n, i, n*i)) 