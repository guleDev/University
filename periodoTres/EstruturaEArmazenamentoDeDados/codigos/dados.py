import mysql.connector

host = "167.99.252.245"
user = "ESW2024_E7"
passwd = "123mudar"
database = "ESW2024_E7"

conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()

def inserirDados():
    varNOME = input("Qual o nome do aluno? -> ")
    varCURSO = input("Qual o curso do aluno? -> ")

    cursor.execute(f"INSERT INTO SALADEAULA (NOME, CURSO) VALUES ('{varNOME}', '{varCURSO}');")
    conector.commit()

def atualizarDAddos():
    vUpd = input("Qual váriavel/coluna vai receber os dados atualizados? -> ")
    vAntigo = input("Qual o item que você quer mudar? -> ")
    vAtual = input("Qual o item atualizado? -> ")

    cmd = f"UPDATE SALADEAULA SET '{vUpd}' = '{vAtual}' WHERE {vUpd} = '{vAntigo}';"

    cursor.execute(cmd)
    conector.commit()

def procurarDados():
    colunaSelect = inpit("Qual a coluna desta tavela para selecionar? -> ")
    cursor.execute(f"SELECT {colunaSelect} FROM SALADEAULA;")

    myresult = cursor.fetchall()

    results = [list(str(item) for item in t) for t in myresult]
    alist = []
    for x in results:
        alist.append(x)
    
    print(alist)
    conector.close()
