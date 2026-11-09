def loja():
    print('Bem-vindo(a) à nossa loja!')
    produto = input('Digite o nome do produto que deseja comprar: ')
    preco = float(input(f'Qual é o preço do {produto}? R$ '))
    quantidade = int(input(f'Quantos {produto}s você deseja comprar? '))
    total = preco * quantidade
    print(f'O total a pagar por {quantidade} {produto}(s) é R$ {total:.2f}.')


def main():
    while True:
        print('\n=== MENU DA LOJA ===')
        print('1 - Comprar produto')
        print('2 - Promoção')
        print('3 - Consultar produto')
        print('4 - Ver estoque')
        print('5 - Realizar venda')
        print('6 - Adicionar ao carrinho')
        print('7 - Cadastrar cliente')
        print('8 - Formas de pagamento')
        print('9 - Ver descontos')
        print('10 - Ver acréscimos')
        print('0 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            loja()
        elif opcao == '2':
            promocao()
        elif opcao == '3':
            produto()
        elif opcao == '4':
            estoque()
        elif opcao == '5':
            venda()
        elif opcao == '6':
            carrinho()
        elif opcao == '7':
            cliente()
        elif opcao == '8':
            pagamento()
        elif opcao == '9':
            desconto()
        elif opcao == '10':
            acrescimo()
        elif opcao == '0':
            print('Saindo do sistema. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')


def promocao():
    print('Aproveite nossa promoção!')
    produto = input('Digite o nome do produto em promoção: ')
    preco = float(input(f'Qual é o preço do {produto}? R$ '))
    desconto = float(input('Qual é a porcentagem de desconto? '))
    preco_final = preco * (1 - desconto / 100)
    print(f'O preço final do {produto} com {desconto}% de desconto é R$ {preco_final:.2f}.')


def produto():
    print('Confira nossos produtos!')
    produto = input('Digite o nome do produto que deseja conferir: ')
    preco = float(input(f'Qual é o preço do {produto}? R$ '))
    print(f'O preço do {produto} é R$ {preco:.2f}.')


def estoque():
    print('Verifique nosso estoque!')
    produto = input('Digite o nome do produto que deseja verificar: ')
    quantidade = int(input(f'Quantos {produto}s temos em estoque? '))
    print(f'Temos {quantidade} {produto}(s) em estoque.')


def venda():
    print('Realize sua venda!')
    produto = input('Digite o nome do produto que deseja vender: ')
    preco = float(input(f'Qual é o preço do {produto}? R$ '))
    quantidade = int(input(f'Quantos {produto}s você deseja vender? '))
    total = preco * quantidade
    print(f'O total da venda de {quantidade} {produto}(s) é R$ {total:.2f}.')


def carrinho():
    print('Adicione produtos ao seu carrinho!')
    produto = input('Digite o nome do produto que deseja adicionar: ')
    preco = float(input(f'Qual é o preço do {produto}? R$ '))
    quantidade = int(input(f'Quantos {produto}s você deseja adicionar ao carrinho? '))
    total = preco * quantidade
    print(f'O total do carrinho com {quantidade} {produto}(s) é R$ {total:.2f}.')


def cliente():
    print('Cadastro de cliente!')
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    print(f'Cliente {nome} cadastrado com sucesso! Email: {email}, Telefone: {telefone}.')


def pagamento():
    print('Escolha a forma de pagamento!')
    print('1 - Dinheiro')
    print('2 - Cartão de Crédito')
    print('3 - Cartão de Débito')


def desconto():
    print('Aproveite nosso desconto especial!')
    print('1 - 10% de desconto')
    print('2 - 20% de desconto')
    print('3 - 30% de desconto')


def acrescimo():
    print('Atenção! Será aplicado um acréscimo no valor da compra.')
    print('1 - 5% de acréscimo')
    print('2 - 10% de acréscimo')
    print('3 - 15% de acréscimo')


if __name__ == "__main__":
    main()