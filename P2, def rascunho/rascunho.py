class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade
        
class Pessoa:
    def __init__(self, nome, contato, especie_interesse, preferencia_animal):
        self.nome = nome
        self.contato = contato
        self.especie_interesse = especie_interesse
        self.preferencia_animal = preferencia_animal
        
class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop(0)

    def esta_vazia(self):
        return len(self.items) == 0
        
#dps so arrumamos o codigo.
def inserir_tipo_animal(dicionario_animais):
    tipo = input("Digite o novo tipo de animal: ")
    dicionario_animais[tipo] = []

def cadastrar_animal(dicionario_animais):
    tipo = input("Digite o tipo do animal: ")
    if tipo in dicionario_animais:
        idade = input("Digite a idade do animal: ")
        cor = input("Digite a cor do animal: ")
        porte = input("Digite o porte do animal: ")
        particularidade = input("Digite alguma particularidade do animal: ")

        animal = Animal(tipo, idade, cor, porte, particularidade)
        dicionario_animais[tipo].append(animal)
        print("Animal cadastrado com sucesso!")
    else:
        print("Tipo de animal não existe.")
