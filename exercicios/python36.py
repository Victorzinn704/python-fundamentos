from datetime import date
ano = int(input('Ano do seu nascimento: '))
idade = date.today().year - ano
if idade < 9:
    print('Voce ja tem {} anos, voce é um nadador MIRIM'.format(idade))
elif idade < 14:
    print('Voce ja tem {} anos, voce é um nadador INFANTIL'.format(idade))
elif idade < 19:
    print('Voce ja tem {} anos, voce é um nadador JUNIOR'.format(idade))
elif idade < 25:
    print('Voce ja tem {} anos, voce é um nadador SÊNIOR'.format(idade))
else:
    print('Voce ja tem {} anos, voce é um nadador MASTER'.format(idade))
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, date.today().year))