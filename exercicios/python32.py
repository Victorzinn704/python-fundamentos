#exercicio de segmentacao de trinagulos
from time import sleep
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
print('Analisando os segmentos...')
sleep(2)  # Simula um atraso na análise
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
if a == b == c:
    print('EQUILÁTERO! Todos os lados são iguais.')
elif a != b != c != a:
    print('ESCALENO! Todos os lados são diferentes.')
else:
    print('ISÓSCELES! Dois lados são iguais.')
