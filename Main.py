class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade


class Pessoa:
    def __init__(self, nome,contato, idade, tipo_animal, idade_animal, cor_animal, porte_animal, particularidade_animal):
        self.nome = nome
        self.contato = contato
        self.idade = idade
        self.tipo_animal = tipo_animal
        self.idade_animal = idade_animal
        self.cor_animal = cor_animal
        self.porte_animal = porte_animal
        self.particularidade_animal = particularidade_animal


  # fazer um sistema para cadastrar animal e pessoa
   # Esse def e o de para inserir novo tipo de animal, pode olhar  e ver se ta tudo certo dps eu finalizo essa parte e mando aq. dps so arrumamos o codigo na segunda.
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


class SistemaAdocao:
    def __init__(self):
        self.animais = []
        self.pessoas = []

    def cadastro_animal(self, tipo, idade, cor, porte, particularidade):
        animal = Animal(tipo, idade, cor, porte, particularidade)
        self.animais.append(animal)
        print('Animal cadastrado com sucesso!')

    def cadastro_pessoa(self, nome, contato, especie_interesse, preferencia):
        pessoa = Pessoa(nome, contato, especie_interesse, preferencia)
        self.pessoas.append(pessoa)
        print('Pessoa cadastrada com sucesso!')

    def buscar_animais_por_caracteristicas(self, especie_interesse, preferencia):
        animais_encontrados = []
        for animal in self.animais:
            if animal.tipo == especie_interesse and animal.cor == preferencia:
                animais_encontrados.append(animal)
        return animais_encontrados

    def gerar_relatorio(self):
        relatorio = "Relatório de cruzamento de espécies disponíveis x possíveis candidatos:\n"
        for pessoa in self.pessoas:
            animais_encontrados = self.buscar_animais_por_caracteristicas(pessoa.especie_interesse, pessoa.preferencia)
            relatorio += f"Nome: {pessoa.nome}\nContato: {pessoa.contato}\nAnimais encontrados:\n"
            if animais_encontrados:
                for animal in animais_encontrados:
                    relatorio += f"Tipo: {animal.tipo}, Cor: {animal.cor}, Porte: {animal.porte}\n"
            else:
                relatorio += "Nenhum animal encontrado\n"
            relatorio += "\n"
        return relatorio
