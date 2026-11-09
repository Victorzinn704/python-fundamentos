n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media >= 6.5:
    print('Voce foi aprovado com a media de {:.2f}. PARABÉNS!' .format(media))
elif media >= 5 and media < 6.5:
    print('Voce esta de recuperacao com a media de {:.2f}, Dá para MELHORAR...' .format(media))
else:
    print('Voce foi reprovado com a media de {:.2f}, Nao fique triste, proximo ano dá para melhorar!' .format(media))