# Bibliotecas
from pymongo import MongoClient
from pymongo import ServerApi
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

database_name = 'UniSenai'
db = client[database_name]
collection_name = "jogos"
collection = db[collection_name]

# ** CREATE ** - Inserir um novo registro à coleção

"""
novo_jogo = {
    "nome": "The Legend of Zelda: Ocarina of Time",
    "plataforma": "Nintendo 64",
    "gênero": "Aventura",
    "desenvolvedor": "Nintendo",
    "ano_lancamento": 1998,
    "avaliacao": 10
}

resultado_insercao = collection.insert_one(novo_jogo)

print(f"Novo jogo inserido com sucesso! ID: {resultado_insercao.inserted_id}")
"""
# ** READ ** - Ler um documento da coleção
"""
consulta = { "nome": "The Legend of Zelda: Ocarina of Time" }
jogo_encontrado = collection.find_one(consulta)
print(f"Jogo encontrado: {jogo_encontrado}")
"""
# ** UPDATE ** - Atualiza um documento
"""
filtro = { "nome": "The Legend of Zelda: Ocarina of Time" }
novo_valor = { "$set": {"avaliacao": 9.9} }
resultado_atualizado = collection.update_one(filtro, novo_valor)

if resultado_atualizado.modified_count > 0:
    print( "Avaliação do jogo atualizada com sucesso!" )
else:
    print("Nenhum documento atualizado!")
"""
# ** Delete ** - 