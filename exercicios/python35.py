from datetime import date
ano = int(input('Ano do seu nascimento: '))
if ano > 18:
    print('Você ainda não tem 18 anos, ainda faltam {} anos para você se alistar'.format(18 - date.today().year + ano))
elif ano == 18:
    print('Você tem 18 anos, está na hora de se alistar!')
else:
    print('Você já passou dos 18 anos, já se passaram {} anos do seu alistamento'.format(date.today().year - ano - 18))
data = date.today().year
print('Quem nasceu em {} tem {} anos em {}'.format(ano, data - ano, data))