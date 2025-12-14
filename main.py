import os
import mysql.connector
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Conexão segura
conexao = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)

print("Banco conectado com sucesso!")