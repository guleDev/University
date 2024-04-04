import mysql.connector

host = "167.99.252.245"
user = "ESW2024_E7"
passwd = "123mudar"
database = "ESW2024_E7"

conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()

def inserirTabela():
    tabela = ''
    add = 's'
    var= 0

    while (tabela != "0"):
        nomeDaTabela = input("Qual o nome da tabela que voce quer criar? --> ")
        cursor.execute(f"CREATE TABLE {nomeDaTabela} (ID INT AUTO_INCREMENT PRIMARY KEY);")

        while (add == 's'):
            add = input("Voce deseja adicionar uma variavel? (S/N) --> ").lower()

            if (add == 's'):
                var = var + 1
                variavelNome = input(f"Digite o nome  da {str(var)}a. variavel? --> ")
                variavelTipo = input(f"Digite o tipo  da {str(var)}a. variavel? --> ")
                cursor.execute(f"ALTER TABLE {nomeDaTabela} ADD {variavelNome} {variavelTipo};")
            elif (add == 'n'):
                tabela = '0'
                print("Good bye...")
                break

inserirTabela()