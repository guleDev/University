from animal import Animal

class Peixe(Animal):
    def __init__(self, nome, raca, peso):
        super().__init__(nome)
        self.raca = raca
        self.peso = peso

    def get_som(self):
        return "Blup!"
    
    def get_peso(self):
        return f'Peso: {self.peso}'
    
    def identidade(self):
        return f'Raça: {self.raca}\nPeso: {self.peso}'
