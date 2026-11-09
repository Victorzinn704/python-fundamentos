class ErroPetShop(Exception):
    pass
class ErroTipoInvalido(ErroPetShop):
    pass
class ErroAnimalNaoEncontrado(ErroPetShop):
    pass

class Vacina:
    def __init__(self, nome, dose):
        self.nome = nome
        self.dose = dose
    
    def __str__(self):
        return f'Vacina: {self.nome}, Dose: {self.dose}'

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.vacinas = []

    def add_vacina(self, vacina):
        if not isinstance(vacina, Vacina):
            raise ErroTipoInvalido("O objeto fornecido não é uma instância da classe Vacina.")
        self.vacinas.append(vacina)

    def listar_vacinas(self):
        return [str(vacina) for vacina in self.vacinas]

    def som (self):
        raise NotImplementedError("O método 'som' deve ser implementado nas subclasses.")
    
    def __str__(self):
        return f'Animal: {self.nome}, Espécie: {self.especie}'
    
class Cachorro(Animal):
    def __init__(self, nome, raça):
        super().__init__(nome, "Cachorro")
        self.raça = raça
    
    def som(self):
        return f'{self.nome}: Au Au!'
    
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")
        self.cor = cor
        
    def som(self):
        return f'{self.nome}: Miau Miau!'
    
class Clinica:
    def __init__(self,nome):
        self.animais = []
        self.nome = nome
    
    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ErroTipoInvalido("O objeto fornecido não é uma instância da classe Animal.")
        self.animais.append(animal)

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
                return animal
        raise ErroAnimalNaoEncontrado(f"Animal com o nome '{nome}' não encontrado na clínica.")
    
    def listar_animais(self):
        return self.animais
    
    def buscar_animal(self, trecho):
        trecho = trecho.lower()
        encontrado = []
    
        for animal in self.animais:
            if trecho in animal.nome.lower():
                encontrado.append(animal)
    
        return encontrado

    def listar_vacinas(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                return animal.listar_vacinas()
        raise ErroAnimalNaoEncontrado(f"Animal com o nome '{nome}' não encontrado na clínica.")
    
try:
    cachorro1 = Cachorro("Rex", "Labrador")
    cachorro2 = Cachorro("Max", "Bulldog")
    gato1 = Gato("Mimi", "Branco")

    cachorro1.add_vacina(Vacina("Raiva", "1ª Dose"))
    cachorro1.add_vacina(Vacina("Cinomose", "2ª Dose"))

    cachorro2.add_vacina(Vacina("Raiva", "1ª Dose"))
    gato1.add_vacina(Vacina("Leucemia Felina", "1ª Dose"))

    gato1.add_vacina(Vacina("Raiva", "1ª Dose"))
    gato1.add_vacina(Vacina("Leucemia Felina", "2ª Dose"))

    clinica = Clinica('Clinica Vida Animal')

    clinica.add_animal(cachorro1)
    clinica.add_animal(cachorro2)
    clinica.add_animal(gato1)

    print("Lista de animais na clínica:")
    for animal in clinica.listar_animais():
        print(animal)
        print("Vacinas:", animal.listar_vacinas())

    print("\nBuscando animais com o nome 'Rex':")
    encontrados = clinica.buscar_animal("Rex")
    for animal in encontrados:
        print(animal)
        print("Vacinas:", animal.listar_vacinas())
    
    print("\nRemovendo o animal 'Max' da clínica.")
    removido = clinica.remover_animal("Max")
    print('Removido', removido)
    print('Vacinas do animal removido:', removido.listar_vacinas())

    print("\nSons dos animais restantes na clínica:")
    for animal in clinica.listar_animais():
        print(animal.som())

    print("\nTestando erro:")
    clinica.add_animal("Não é um animal")

except ErroAnimalNaoEncontrado as erro:
    print("Erro: animal não encontrado:", erro)
except ErroTipoInvalido as erro:
    print("Erro de tipo inválido:", erro)