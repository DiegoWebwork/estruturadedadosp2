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

        
        
        
