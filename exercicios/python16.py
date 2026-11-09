n1 = float(input('sua primeira nota: '))
n2 = float(input('sua segunda nota: '))
media = (n1+n2)/2
if media >= 7:
    print('Voce foi aprovado com a media de {:.2f}' .format(media))
elif media >= 5 and media < 7:
    print('Voce esta de recuperacao com a media de {:.2f}' .format(media))
else:
    print('Voce foi reprovado com a media de {:.2f}' .format(media)) 