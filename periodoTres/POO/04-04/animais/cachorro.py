from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def get_som(self):
        return "Au Au!"

    def identidade(self):
        return f'Nome: {self.nome} \nRaça: {self.raca}'
