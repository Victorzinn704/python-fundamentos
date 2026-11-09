peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está abaixo do peso! Seu IMC é {:.1f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal! Seu IMC é {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('Você está com sobrepeso! Seu IMC é {:.1f}'.format(imc))
elif 30 <= imc < 40:
    print('Você está com obesidade! Seu IMC é {:.1f}'.format(imc))
else:
    print('Você está com obesidade mórbida! Seu IMC é {:.1f}'.format(imc))
print('Sua altura é {:.2f}m e seu peso é {:.1f}Kg'.format(altura, peso))
print('Voce precisa perder {:.1f}Kg para atingir o peso ideal'.format(peso - (25 * (altura ** 2))))