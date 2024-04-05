from animal import Animal
from cachorro import Cachorro
from peixe import Peixe
from galinha import Galinha

def fazer_barulho(animal):
    print(animal.get_som())

def mostrar_identidade(animal):
    print(animal.identidade())

# Instâncias de Animal e Cachorro
animal = Animal("Animal")
cachorro = Cachorro("Jorel", "Viralata caramelo")
galinha = Galinha("Pintadinha", "Galinha d'Angola")

# Chama o método get_som em cada objeto
fazer_barulho(animal)
fazer_barulho(cachorro)
fazer_barulho(galinha)
mostrar_identidade(galinha)