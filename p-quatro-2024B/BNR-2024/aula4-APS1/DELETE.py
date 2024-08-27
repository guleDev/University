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

# 2.D. DELETE 01 - Remover todos os projetos com orçamento menor que R$ 50.000.
filtro = {"orcamento": {"$lt": 50000}}
resultado_delecao = collection.delete_many(filtro)
print(filtro)
if resultado_delecao.deleted_count > 0:
    print("Projetos deletados com sucesso.")
else:
    print("Nenhum documento foi deletado.")

# Fechar a conexão com o MongoDB
client.close()