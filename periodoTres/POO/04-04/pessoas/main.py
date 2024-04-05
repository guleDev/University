from aluno import Aluno
from professor import Professor

def apresentar_pessoa(pessoa):
    print(pessoa.apresentar())

aluno = Aluno('João', '12345')
professor = Professor('Paulo', 'Corte e Costura')

apresentar_pessoa(aluno)
apresentar_pessoa(professor)