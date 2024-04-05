import mysql.connector

host = "167.99.252.245"
user = "ESW2024_E7"
password = "123mudar"
database = "ESW2024_E7"

conector = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conector.cursor()
def inserirDados():
    tabelaInsert = input("Em qual tabela você quer inserir os dados -> ")
    variavelInsert = input("Qual variável/coluna vai receber os dados -> ")
    valorInsert = input("Qual o valor a ser inserido na variável/coluna -> ")
    print("Good bye...")
    
    cursor.execute(f"INSERT INTO {tabelaInsert} ({variavelInsert}) VALUES ({valorInsert});")
    conector.commit()

def alunoCurso():
    varAluno_ID = input("Insira o ID do aluno -> ")
    varCurso_ID = input("Insira o ID do curso do aluno -> ")
    print("Good bye...")
    
    cursor.execute(f"INSERT INTO AlunoCurso (aluno_id, curso_id) VALUES ({varAluno_ID}, {varCurso_ID});")
    conector.commit()

def curso():
    varNome = input("Insira o nome do curso -> ")
    varProfessor = input("Insira o nome do professor para o curso-> ")
    varCarga_Horaria = input("Insira a carga horaria do curso -> ")
    varPeriodos = input("Quantos periodos tem o curso -> ")
    print("Good bye...")

    cursor.execute(f"INSERT INTO Curso (nome, professor, carga_horaria, periodos) VALUES ('{varNome}', '{varProfessor}', '{varCarga_Horaria}', {varPeriodos});")
    conector.commit()

def endereco():
    varCEP = input("Insira o CEP -> ")
    varEstado = input("Insira o estado ->")
    varUF = input("Insira o UF do estado -> ")
    varCidade = input("Insira a cidade -> ")
    varBairro = input("Insira o bairro-> ")
    varRua = input("Insira o nome da rua -> ")
    varNumero = input("Insira o numero da residencia -> ")
    varComplemento = input("Insira um complemento -> ")
    print("Good bye...")

    cursor.execute(f"INSERT INTO Endereco (cep, estado, uf, cidade, bairro, rua, numero, complemento) VALUES ('{varCEP}', '{varEstado}', '{varUF}', {varCidade}, '{varBairro}', '{varRua}', {varNumero}, '{varComplemento}');")
    conector.commit()