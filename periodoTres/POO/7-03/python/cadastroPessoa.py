# Definição da classe Pessoa
class Pessoa:
    # Método especial de inicialização (__init__)
    # que é chamado ao criar uma nova instância da classe
    def __init__(self, nome, idade, cidade):
        # Inicializa os atributos da instância com os valores passados como argumento
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    # Método da classe Pessoa formatada com o nome e idade da pessoa
    def apresentar(self):
    #Inprime uma mensagem formatada com o nome e dade da pessoa
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos e moro em {self.cidade}")

# Criando objetos (instâncias) da classe Pessoa
pessoa1 = Pessoa("Alice", 25, "Blumenau")
pessoa2 = Pessoa("Bob", 30, "Curitiba")
pessoa3 = Pessoa("Dudu", 18, "São José dos Pinhais")
pessoa4 = Pessoa("Cássia", 84, "Colombo")

# Chamando o método da classe para cada objeto, exibindo as informações
pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()
pessoa4.apresentar()
