class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def infoCarro(self):
        print(f"modelo: {self.modelo}, ano: {self.ano}, cor: {self.cor}")

carro1 = Carro("chevrolet", 1978, "marrom")
carro1.infoCarro()