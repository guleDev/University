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
# 2.A. CREATE 01 - Adicionar um novo documento na coleção projetos.
novo_projeto = {
        "nome": "Desenvolvimento de Aplicativo Móvel",
        "metodologia": "Ágil",
        "tecnologias": "Kotlin, Swift,React Native",
        "orcamento": 50000,
        "data_conclusao": "2024-12-31",
        "lider_projeto": "Sandro de Araujo"
    }

resultado_insercao = collection.insert_one(novo_projeto)
print(f"Novo projeto inserido com ID: {resultado_insercao.inserted_id}")

# Fechar a conexão com o MongoDB
client.close()