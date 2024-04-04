class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
class Passaro(Animal):
    def emitir_som(self):
        return "Piu piu!"
    
#Exemplo de uso
cachorro1 = Cachorro("Jorel")
cachorro2 = Cachorro("Robson")

print(f"{cachorro1.nome}: {cachorro1.emitir_som()}")
print(f"{cachorro2.nome}: {cachorro2.emitir_som()}")

gato1 = Gato("Magali")
gato2 = Gato("Furico")
print(f"{gato1.nome}: {gato1.emitir_som()}")
print(f"{gato2.nome}: {gato2.emitir_som()}")

passaro1 = Passaro("Chuck")
passaro2 = Passaro("Loro")
print(f"{passaro1.nome}: {passaro1.emitir_som()}")
print(f"{passaro2.nome}: {passaro2.emitir_som()}")
