import mysql.connector
import pandas as pd
from tabulate import tabulate

host = "167.99.252.245"
user = "ESW2024_E7"
password = "123mudar"
database = "ESW2024_E7_AUTOTECH"

conector = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conector.cursor()

def cadastrarPeca():
    print("Insira as informações da peça!")
    peca = input("Peça para cadastro -> ")
    marca = input("Marca da peça cadastrada -> ")
    modelo = input("Modelo da peça cadastrada -> ")
    quantidade = input("Quantidade de peças para cadastrar -> ")
    preco = input("Preço da peça cadastrada -> R$ ")
    print("Dados inseridos com sucesso!")

    cadastro = f"INSERT INTO InventarioPecas (peca, marca, modelo, quantidade, preco_unitario) VALUES ('{peca}', '{marca}', '{modelo}', {quantidade}, {preco});"
    
    cursor.execute(cadastro)
    conector.commit()

def atualizarEstoque():
    atualizar = input("""1 - Entrada
2 - Saída
""")
    match atualizar:
        case "1":
            print("Entrada")
        case "2":
            print("Saída")
        case _:
            print("Opção inválida")
            atualizarEstoque()

def escolherRelatorioEstoque():
    relatorio = input("""Opções de relátorio
                      
1 - Relatório geral
2 - Relatório quantidade de peças
3 - Relatório quantidade de peças por marca
4 - Relatório quantidade de peças por modelo
5 - Relatório valor do estoque
""")
    
    match relatorio:
        case "1":
            print("Relatório geral")
            cmd = "SELECT * FROM InventarioPecas;"
            relatorioGeral(cmd)
        case "2":
            print("Relatório quantidade de peças")
            pecaPull = input("Informe a peça para o relatório -> ")
            cmd = f"SELECT * FROM InventarioPecas WHERE peca = '{pecaPull}';"
            relatorioQtdPecas(cmd, pecaPull)
        case "3":
            print("Relatório quantidade de peças por marca")
            marcaPull = input("Informe a marca para o relatório -> ")
            cmd = f"SELECT * FROM InventarioPecas WHERE marca = '{marcaPull}';"
            relatorioQtdPecasMarca(cmd)
        case "4":
            print("Relatório quantidade de peças por modelo")
            modeloPull = input("Informe o modelo para o relatório -> ")
            cmd = f"SELECT * FROM InventarioPecas WHERE modelo = '{modeloPull}';"
            relatorioQtdPecasModelo(cmd, modeloPull)
        case "5":
            print("Relatório valor do estoque")
            cmd = "SELECT * FROM InventarioPecas;"
            relatorioValorEstoque(cmd)
        case _:
            print("Opção inválida")
            escolherRelatorioEstoque()

def relatorioGeral(cmd):
    cursor.execute(cmd)
    myresult = cursor.fetchall()
    df = pd.DataFrame(myresult, columns=["ID", "peça", "marca", "modelo", "quantidade", "preço unitário"])
    print(tabulate(df, headers='keys',tablefmt="psql"))

def relatorioQtdPecas(cmd, pecaPull):
    cursor.execute(cmd)
    myresult = cursor.fetchall()
    df = pd.DataFrame(myresult, columns=["ID", "peça", "marca", "modelo", "quantidade", "preço unitário"])
    df['TOTAL'] = df['quantidade']
    soma = sum(df['TOTAL'])
    df['TOTAL'] = df['quantidade'] * df['preço unitário']
    somaValor = sum(df['TOTAL'])
    print(tabulate(df, headers='keys',tablefmt="psql"))
    print(f'TOTAL DA PEÇA "{pecaPull.upper()}": {soma}')
    print(f'VALOR TOTAL DE PEÇAS DA MARCA "{pecaPull.upper()}": R$ {somaValor:.2f}')

def relatorioQtdPecasMarca(cmd, marcaPull):
    cursor.execute(cmd)
    myresult = cursor.fetchall()
    df = pd.DataFrame(myresult, columns=["ID", "peça", "marca", "modelo", "quantidade", "preço unitário"])
    df['TOTAL'] = df['quantidade']
    somaPeca = sum(df['TOTAL'])
    df['TOTAL'] = df['quantidade'] * df['preço unitário']
    somaValor = sum(df['TOTAL'])
    print(tabulate(df, headers='keys',tablefmt="psql"))
    print(f'TOTAL DE PEÇAS DA MARCA "{marcaPull.upper()}": {somaPeca}')
    print(f'VALOR TOTAL DE PEÇAS DA MARCA "{marcaPull.upper()}": R$ {somaValor:.2f}')

def relatorioQtdPecasModelo(cmd, modeloPull):
    cursor.execute(cmd)
    myresult = cursor.fetchall()
    df = pd.DataFrame(myresult, columns=["ID", "peça", "marca", "modelo", "quantidade", "preço unitário"])
    df['TOTAL'] = df['quantidade']
    somaPeca = sum(df['TOTAL'])
    df['TOTAL'] = df['quantidade'] * df['preço unitário']
    somaValor = sum(df['TOTAL'])
    print(tabulate(df, headers='keys',tablefmt="psql"))
    print(f'TOTAL DE PEÇAS DO MODELO "{modeloPull.upper()}": {somaPeca}')
    print(f'VALOR TOTAL DE PEÇAS DA MARCA "{modeloPull.upper()}": R$ {somaValor:.2f}')

def relatorioValorEstoque(cmd):
    cursor.execute(cmd)
    myresult = cursor.fetchall()
    df = pd.DataFrame(myresult, columns=["ID", "peça", "marca", "modelo", "quantidade", "preço unitário"])
    df['TOTAL'] = df['quantidade'] * df['preço unitário']
    soma = sum(df['TOTAL'])
    print(tabulate(df, headers='keys',tablefmt="psql"))
    print(f'VALOR TOTAL DO ESTOQUE: R$ {soma:.2f}')

escolherRelatorioEstoque()
