class clinica: 
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    # metodos de instancia

    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        return (f'Olá {self.nome}, você tem {self.idade} anos, seu sexo é {self.sexo}, seu peso é {self.peso}Kg e sua altura é {self.altura}m.')
    

# declaracao do objeto
paciente = clinica('João', 25, 'Masculino', 70, 1.75)
paciente2 = clinica('Maria', 30, 'Feminino', 60, 1.65)
paciente.aniversario()
paciente2.aniversario()
print(paciente.mensagem())
print(paciente2.mensagem())