class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_info(self):
        return f'Funcionário: {self.nome}, Salário: R${self.salario:.2f}'

class EngenheiroDeSoftware(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_info(self):
        return f'Engenheiro de Software: {self.nome}, Salário: R${self.salario:.2f}, Departamento: {self.departamento}'
    
class Programador(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_info(self):
        return f'Programador: {self.nome}, Salário: R${self.salario:.2f}, Linguagem: {self.linguagem}'
    
# Exemplo de uso
        
engenheiroDeSoftware1 = EngenheiroDeSoftware('Maria', 20000, 'Desenvolvimento')
print(engenheiroDeSoftware1.exibir_info())

programador1 = Programador('João', 5000, 'Python')
print(programador1.exibir_info())
