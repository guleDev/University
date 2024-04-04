class Animal:
    def __init__(self, tipo, cor, som_padrao):
        self.tipo = tipo
        self.cor = cor
        self.som_padrao = som_padrao

    def som(self):
        print(self.som_padrao)

    def exibirInfo(self):
        print("Tipo: ", self.tipo)
        print("Cor: ", self.cor, "\n")

# Criando um objeto da classe Animal para representar um cachorro
meuCachorro = Animal("Mamifero", "Marrom", "Au au!")
meuCachorro.som() # Chamando o método som para fazer o cachorro latir
meuCachorro.exibirInfo() # Exibindo informações sobre o cachorro

# Criando um objeto da classe Animal para representar um gato
meuGato = Animal("Mamifero", "Branco", "Miau miau!") 
meuGato.som() # Chamando o método som para fazer o gato miar
meuGato.exibirInfo() # Exibindo informações sobre o gato