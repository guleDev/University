import mysql.connector

host = "167.99.252.245"
user = "ESW2024_E7"
passwd = "123mudar"
database = "ESW2024_E7_HiperPampus"

conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

cursor = conector.cursor()

def tabelaClientes():
  nome = input('Nome: ')
  cpf = input('CPF: ')
  carro = input('Placa do veiculo: ')
  endereco = input('Endereço: (cep) ')
  fidelidade = input('Fidelidade: ')

  cursor.execute(f"INSERT INTO clientes (nome, cpf, carro, endereco, fidelidade) VALUES ('{nome}', '{cpf}', '{carro}', '{endereco}', {fidelidade});")
  conector.commit()
  print('\nValores Inseridos')

def tabelaCarro():
  cliente_id = input('ID do cliente: ')
  placa = input('Placa: ')
  marca = input('Marca: ')
  modelo = input('Modelo: ')
  ano = input('Ano: ')
  manutencao = input('Manutenção necessária: ')

  cursor.execute(f"INSERT INTO carro (cliente_id, placa, marca, modelo, ano, manutencao) VALUES ({cliente_id} ,'{placa}', '{marca}', '{modelo}', {ano}, '{manutencao}');")
  conector.commit()
  print('\nValores Inseridos')

def tabelaEstoque():
  produto = input('Nome do produto: ')
  quantidade = input('Quantidade total: ')
  qualidade = input('Qualidade: ')
  fluxo_entrada = input('Quantidade de entrada: ')
  fluxo_saida = input('Quantidade de saida: ')
  lucro = input('Lucro: ')

  cursor.execute(f"INSERT INTO estoque (produto, quantidade, qualidade, fluxo_entrada, fluxo_saida, lucro) VALUES ('{produto}', {quantidade}, '{qualidade}', {fluxo_entrada}, {fluxo_saida}, '{lucro}');")
  conector.commit()
  print('\nValores Inseridos')

def atualizarTabela(tabelaAtualizar):
    colunaAtualizar = input('Qual variável/coluna vai receber os dados atualizados? ')
    valorAtualizar = input('Qual o valor que você quer mudar? ')
    valorAtualizado = input('Qual o novo valor? ')

    cursor.execute(f"UPDATE {tabelaAtualizar} SET {colunaAtualizar} = %s WHERE {colunaAtualizar} = %s", (valorAtualizado, valorAtualizar))
    conector.commit()
    print("\nProcesso Concluído!")

def procurarTabela(tabelaProcura):
    coluna = input("Qual a coluna desta tabela para selecionar? ")
    cursor.execute(f"SELECT {coluna} FROM {tabelaProcura};")

    myresult = cursor.fetchall()

    resultado = [lista(str(item) for item in t) for t in myresult]
    lista = []
    for x in resultado:
        lista.append(x)

    print(lista)
    conector.close()

while True:
  tabela = int(input("""Desejar adicionar dados a qual tabela?
1. CLIENTES
2. ESTOQUE
3. CARRO
4. ATUALIZAR TABELAS
5. LISTAR UMA COLUNA
6. SAIR
"""))
  if tabela  == 1:
    tabelaClientes()

  elif tabela == 2:
    tabelaEstoque()

  elif tabela == 3:
    tabelaCarro()

  elif tabela == 4:
    tabelaAtualizar = input('Digite o nome da tabela que deseja atualizar: ')
    atualizarTabela(tabelaAtualizar)

  elif tabela == 5:
    tabelaProcura = input('Digite o nome da tabela que deseja procurar: ')
    procurarTabela(tabelaProcura)

  elif tabela == 6:
    print('Programa fechado!')
    break
