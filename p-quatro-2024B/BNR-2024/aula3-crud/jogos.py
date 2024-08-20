# Bibliotecas
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import json

# Carregar e ler arquivo JSON
with open ('config.json') as config_file:
    config = json.load(config_file)

# Credenciais e URI base
username = config['MONGO_USERNAME']
password = config['MONGO_PASSWORD']

# Escape o nome de usuário e a senha
username = quote_plus(username)
password = quote_plus(password)

# URI de conexão
uri = f"mongodb://guledev64:<password>@<hostname>/?ssl=true&replicaSet=atlas-14j2ke-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster1"

# Criar novo cliente e conectar-se ao servidor
client = MongoClient(uri, server_api=ServerApi('1'))

# Definir o nome do banco de dados
database_name = 'UniSenai'
db = client[database_name]

# Definir o nome da nova coleção
collection_name = "jogos"
collection = db[collection_name]

# Carregar o json dos produtos
with open('jogos.json', encoding='utf-8') as jogos_file:
    jogos = json.load(jogos_file)

# Inserir os produtos no banco
if isinstance(jogos, list): # Verificar se é uma lista de documentos
    result = collection.insert_many(jogos)
    print(f'{len(result.inserted_ids)} documentos na coleção! "{collection_name}" com sucesso!')
else:
    print('O arquivo JSON não comtém documentos')

# Fechar a conexão
client.close()