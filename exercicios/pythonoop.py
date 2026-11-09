class Banco:
    def __init__(self, usuario, saldo):
        self.usuario = usuario
        self.saldo = saldo

    def depositar(self, deposito):
        if deposito > 0:
            self.saldo += deposito
            print(f"Depósito de R${deposito} realizado com sucesso!")
            return self.saldo
        else:
            print("Valor de depósito inválido.")
            return self.saldo

    def sacar(self, sacar):
        if sacar > 0 and sacar <= self.saldo:
            self.saldo -= sacar
            print(f"Saque de R${sacar} realizado com sucesso!")
            return self.saldo
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
            return self.saldo

    def transferencia(self, valor, destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            print(f"Transferência de R${valor} realizada com sucesso para {destino.usuario}!")
            return self.saldo
        else:
            print("Saldo insuficiente ou valor de transferência inválido.")
            return self.saldo

joao = Banco("João", 1000)
maria = Banco("Maria", 500)

joao.transferencia(300, maria)

print(joao.saldo)
print(maria.saldo)