from animal import Animal

class Galinha(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def get_som(self):
        return "Pó Pó!"
    
    def identidade(self):
        return f'Nome: {self.nome} \nRaça: {self.raca}'
