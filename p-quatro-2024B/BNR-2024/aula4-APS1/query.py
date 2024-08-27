# Bibliotecas
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import json

# Carregar e ler o arquivo JSON de configuração
with open('config.json') as config_file:
    config = json.load(config_file)

# Credenciais e URI base
username = config['MONGO_USERNAME']  
password = config['MONGO_PASSWORD']        

# Escape o nome de usuário e a senha
username = quote_plus(username)
password = quote_plus(password)

# URI de conexão
uri = f"mongodb+srv://{username}:{password}@cluster1.rfbhp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

# Criar novo cliente e conectar-se ao servidor
client = MongoClient(uri, server_api=ServerApi('1'))

# Definir o nome do banco de dados
database_name = 'gestaoProjetos'
db = client[database_name]

# Definir o nome da coleção
collection_name = 'projetos'
collection = db[collection_name]

# 2.B. QUERY 01 - Consultar todos os documentos na coleção projetos, e que tenham como metodologia o método Ágil.
# query = {"metodologia": "Ágil"}
# projetos_filtro = collection.find(query, {"nome": 1, "metodologia": 1, "_id": 0})
# print(f"Projetos com metodo Ágil:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.A. QUERY 01 - Projetos com orçamento acima de R$ 100.000.
# query = {"orcamento": {"$gt": 100000}}
# projetos_filtro = collection.find(query, {"nome": 1, "orcamento": 1, "_id": 0})
# print(f"Projetos com orçamento maior que R$ 100.000:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.B. QUERY 02 - Consultas de projetos que usam tecnologias baseadas em Firebase.
# query = {"tecnologias": "Firebase"}
# projetos_filtro = collection.find(query, {"nome": 1, "tecnologias": 1, "_id": 0})
# print(f"Projetos que usam tecnologias baseadas em Firebase:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.C. QUERY 03 - Projetos com orçamento entre R$ 80.000 e R$ 100.000.
# query = {"orcamento": {"$gt": 80000, "$lt": 100000}}
# projetos_filtro = collection.find(query, {"nome": 1, "orcamento": 1, "_id": 0})
# print(f"Projetos com orçamento entre R$ 80.000 e R$ 100.000:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.D. QUERY 04 - Projetos que têm a metodologia Scrum e orçamento acima de R$ 100.000.
# query = {"metodologia": "Scrum", "orcamento": {"$gt": 100000}}
# projetos_filtro = collection.find(query, {"nome": 1, "metodologia": 1, "orcamento": 1, "_id": 0})
# print(f"Projetos com metodologia Scrum e orçamento acima de R$ 100.000:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.E. QUERY 05 - Projetos concluídos antes de 01/01/2024.
# query = {"data_conclusao": {"$lt": "2024-01-01"}}
# projetos_filtro = collection.find(query, {"nome": 1, "data_conclusao": 1, "orcamento": 1, "_id": 0})
# print(f"Projetos concluídos antes de 01/01/2024:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.F. QUERY 06 - Projetos com metodologia Waterfall que usam SQL Server.
# query = {"metodologia": "Waterfall", "tecnologias": "SQL Server"}
# projetos_filtro = collection.find(query, {"nome": 1, "metodologia": 1, "tecnologias": 1, "_id": 0})
# print(f"Projetos com metodologia Waterfall que usam SQL Server:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.G. QUERY 07 - Projetos com o nome que contém a palavra Sistema. Utilize o operador regex.
# query = {"nome": {"$regex": "Sistema"}}
# projetos_filtro = collection.find(query, {"nome": 1, "_id": 0})
# print(f"Projetos com o nome que contém a palavra Sistema:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.H. QUERY 08 - Projetos que utilizam as tecnologias Python e Flask. Utilize o operador all.
# query = {"tecnologias": {"$all": ["Python", "Flask"]}}
# projetos_filtro = collection.find(query, {"nome": 1, "tecnologias": 1, "_id": 0})
# print(f"Projetos com as tecnologias Python e Flask:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.I. QUERY 09 - Projetos liderados por Adrian Netto ou Allan Pacheco. Utilize o operador in.
# query = {"lider_projeto": {"$in": ["Adrian Netto", "Allan Pacheco"]}}
# projetos_filtro = collection.find(query, {"nome": 1, "lider_projeto": 1, "_id": 0})
# print(f"Projetos liderados por Adrian Netto ou Allan Pacheco:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.J. QUERY 10 - Projetos que utilizam "Node.js" e foram finalizados antes de 2024.
# query = {"tecnologias": "Node.js", "data_conclusao": {"$lt": "2024-01-01"}}
# projetos_filtro = collection.find(query, {"nome": 1, "tecnologias": 1, "data_conclusao": 1,"_id": 0})
# print(f"Projetos que utilizam Node.js e foram finalizados antes de 2024:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.K. QUERY 11 - Média de orçamento dos projetos que desenvolvidos com a metodologia Ágil.
# pipeline = [
#     {"$match": {"metodologia": "Ágil"}},
#     {"$group": {"_id": None, "media_orcamentos": {"$avg": "$orcamento"}}}
# ]
# resultado = list(collection.aggregate(pipeline))
# if resultado:
#     media_orcamentos = resultado[0]["media_orcamentos"]
#     print(f"Média de orçamentos da metodologia Àgil: {media_orcamentos}")

# 3.L. QUERY 12 - Todos os projetos desenvolvidos com a metodologia Waterfall.
# query = {"metodologia": "Waterfall"}
# projetos_filtro = collection.find(query, {"nome": 1, "metodologia": 1, "_id": 0})
# print(f"Projetos desenvolvidos com a metodologia Waterfall:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.M. QUERY 13 - Qual o projeto com o maior orçamento?
# sort_criteria = [("orcamento", -1)]
# maior_orcamento = collection.find_one({}, sort=sort_criteria, projection={"nome": 1, "orcamento": 1, "_id": 0})
# if maior_orcamento:
#     print(f"Projeto com maior orçamento: {maior_orcamento['nome']}, Valor orçamento {maior_orcamento['orcamento']}")

# 3.N. QUERY 14 - Qual a metodologia com o maior número de projeto? Combinar os operadores unwind, group, sort e limit.
# pipeline = [
#     {"$unwind": "$metodologia"},
#     {"$group": {"_id": "$metodologia", "count": {"$sum": 1}}},
#     {"$sort": {"count": -1}},
#     {"$limit": 1}
# ]
# resultado = list(collection.aggregate(pipeline))
# if resultado:
#     metodologia = resultado[0]["_id"]
#     count = resultado[0]["count"]
#     print(f"Metodologia com mais projetos: {metodologia} com {count} projetos")

# 3.O. QUERY 15 - Todos os projetos que utilizam Ruby e Rails como tecnologias.
# query = {"tecnologias": {"$in": ["Ruby", "Rails"]}}
# projetos_filtro = collection.find(query, {"nome": 1, "tecnologias": 1, "_id": 0})
# print(f"Projetos com metodo Ruby e Rails:")
# for projeto in projetos_filtro:
#     print(projeto)

# 3.P. QUERY 16 - Quais são os projetos desenvolvidos com Kanban e que têm um orçamento menor que R$ 80.000?
query = {"metodologia": "Kanban", "orcamento": {"$lt": 80000}}
projetos_filtro = collection.find(query, {"nome": 1, "tecnologias": 1, "orcamento": 1, "_id": 0})
print(f"Projetos desenvolvidos com Kanban e que têm um orçamento menor que R$ 80.000:")
for projeto in projetos_filtro:
    print(projeto)

# Fechar a conexão com o MongoDB
client.close()
