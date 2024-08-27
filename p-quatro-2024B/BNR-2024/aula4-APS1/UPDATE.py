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

# 2.C. UPDATE 01 - Atualizar o valor do orçamento para o projeto adicionado, alterando o valor para R$ 60.000,00. Posteriormente, atualizar a data de conclusão (30/11/2024) e o líder (Judite Glavatzki).

filtro = {"nome": "Desenvolvimento de Aplicativo Móvel"}
novo_valor = {"$set": {"orcamento": 60000, "data_conclusao": "2024-11-30", "lider_projeto": "Judite Glavatzki"}}
resultado_atualizacao = collection.update_one(filtro, novo_valor)
if resultado_atualizacao.modified_count > 0:
    print("[ Orçamento, data de conclusão e lider de projeto ] atualizadas com sucesso.")
else:
    print("Nenhum documento foi atualizado.")

# Fechar a conexão com o MongoDB
client.close()