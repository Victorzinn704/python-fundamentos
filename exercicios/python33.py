# Empréstimo aprovado na hora até 30% do salário.
# De 31% até 40%, fica sujeito a análise ou fiador.
# Acima de 40%, negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestacao))
print('O valor da prestação corresponde a {:.2f}% do salário.'.format((prestacao / salario) * 100))

if prestacao <= salario * 0.30:
    print('Empréstimo APROVADO NA HORA!')
elif prestacao <= salario * 0.40:
    print('Empréstimo sujeito a aprovação mediante análise ou fiador!')
else:
    print('Empréstimo NEGADO!')