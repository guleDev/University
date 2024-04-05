from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

    def apresentar(self):
        return f'{super().apresentar()} e sou aluno, minha matrícula é {self.matricula}'