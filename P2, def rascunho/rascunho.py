#a importação de sys é usada para chamar a função sys.exit(1) no caso de uma entrada inválida do usuário, 
#interrompendo a execução do programa com um código de saída 1. Isso é uma maneira de lidar com erros e terminar o programa de forma controlada.
import sys

# Classe para representar um animal
class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

# Classe para representar uma pessoa interessada em adotar
class Interessado:
    def __init__(self, nome, contato, especie, preferencia):
        self.nome = nome
        self.contato = contato
        self.especie = especie
        self.preferencia = preferencia
        print("Tipo de animal não existe.")
        
  # Classe para representar o sistema de adoção
class SistemaAdocao:
    def __init__(self):
        self.animais = []
        self.interessados = []
        
# Método para cadastrar um animal
    def cadastrar_animal(self, animal):
        self.animais.append(animal)        
# Método para cadastrar um interessado
    def cadastrar_interessado(self, interessado):
        self.interessados.append(interessado)
        
# Método para pesquisar animal por características
    def pesquisar_animal(self, tipo, idade, cor, porte, particularidade):
        resultados = []
        for animal in self.animais:
            if (
                animal.tipo == tipo
                and animal.idade == idade
                and animal.cor == cor
                and animal.porte == porte
                and animal.particularidade == particularidade
            ):
                resultados.append(animal)
        return resultados
    
    # Método para gerar relatório de cruzamento de espécies disponíveis x possíveis candidatos
    def gerar_relatorio(self):
        relatorio = []
        for interessado in self.interessados:
            candidatos = self.pesquisar_animal(
                interessado.especie,
                None,
                None,
                None,
                interessado.preferencia
            )
            relatorio.append((interessado, candidatos))
        return relatorio
    
    # Função para tratar erros de entrada inválida do usuário
def tratar_erro():
    print("Entrada inválida. Tente novamente.")
    sys.exit(1)
    
def exibir_menu():
    print("=== Sistema de Adoção de Animais ===")
    print("1. Cadastrar animal")
    print("2. Cadastrar interessado")
    print("3. Pesquisar animal por características")
    print("4. Gerar relatório")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha
# Função para cadastrar um animal
def cadastrar_animal(sistema):
    tipo = input("Tipo do animal: ")
    idade = input("Idade aproximada: ")
    cor = input("Cor: ")
    porte = input("Porte: ")
    particularidade = input("Particularidade: ")
    
# Função para cadastrar um interessado
def cadastrar_interessado(sistema):
    nome = input("Nome: ")
    contato = input("Contato: ")
    especie = input("Espécie de animal desejada: ")
    preferencia = input("Preferência do animal: ")
    interessado = Interessado(nome, contato, especie, preferencia)
    sistema.cadastrar_interessado(interessado)
    print("Interessado cadastrado com sucesso!")
    
 def pesquisar_animal(sistema):
    tipo = input("Tipo do animal: ")
    idade = input("Idade aproximada: ")
    cor = input("Cor: ")
    porte = input("Porte: ")
    particularidade = input("Particularidade: ")
    resultados = sistema.pesquisar_animal(tipo, idade, cor, porte, particularidade)
    if len(resultados) > 0:
        print("Animais encontrados:")
        for animal in resultados:
            print(animal.tipo, animal.idade, animal.cor, animal.porte, animal.particularidade)
    else:
        print("Nenhum animal encontrado.")
    
 # Função para gerar relatório
def gerar_relatorio(sistema):
    relatorio = sistema.gerar_relatorio()
    if len(relatorio) > 0:
        print("Relatório de cruzamento de espécies disponíveis x possíveis candidatos:")
        for interessado, candidatos in relatorio:
            print("Interessado:", interessado.nome, interessado.contato)
            print("Candidatos:")
            for animal in candidatos:
                print(animal.tipo, animal.idade, animal.cor, animal.porte, animal.particularidade)
    else:
        print("Nenhum interessado cadastrado.")
        
# Função principal
def main():
    sistema = SistemaAdocao()
    while True:
        escolha = exibir_menu()
        if escolha == "1":
            cadastrar_animal(sistema)
        elif escolha == "2":
            cadastrar_interessado(sistema)
        elif escolha == "3":
            pesquisar_animal(sistema)
        elif escolha == "4":
            gerar_relatorio(sistema)
        elif escolha == "5":
            sys.exit(0)
        else:
            tratar_erro()
