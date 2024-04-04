class Pessoa: # Classe
    def __init__(self, nome, idade): # Método para criar a classe
        self.nome = nome
        self.idade = idade
    
    def exibir_info(self): # Método
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

# Cria duas instâncias da classe Pessoa
pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

# Chamando o método exibir_info() para cada instância
pessoa1.exibir_info()
print()
pessoa2.exibir_info()
