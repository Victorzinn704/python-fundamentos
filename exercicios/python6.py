p1 = float(input('digite a sua primeira nota: '))
p2 = float(input('digite a sua segunda nota; '))
m = (p1+p2)/2
if m < 5.0:
    print('A sua media foi de {:.1f} e voce foi reprovado!' .format(m))
elif m >= 5.0 and m < 6.9:
    print('A sua media foi de {:.1f} e voce esta de recuperacao!' .format(m))
else:
    print('A sua media foi de {:.1f} e voce foi aprovado!' .format(m))