class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        return f'Veiculo: {self.marca} {self.modelo}'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def descrever(self):
        return f'Carro: {self.marca} {self.modelo}, Cor: {self.cor}'
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def descrever(self):
        return f'Moto: {self.marca} {self.modelo}, Cilindrada: {self.cilindrada}cc'
    
#Exemplo de uso
carro1 = Carro('Toyota', 'Corolla', 'Preto')
carro2 = Carro('Honda', 'Accord', 'Branco')
print(carro1.descrever())
print(carro2.descrever())

moto1 = Moto('Honda', 'CBR600RR', 600)
moto2 = Moto('Honda', 'CG160', 160)
print(moto1.descrever())
print(moto2.descrever())
