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
print(" ")
cursor = conexao.cursor()

print("Bem vindo ao sistema de vendas!")
print("O que deseja fazer?")
print("1 - Cadastrar produto")
print("2 - Listar produtos")
print("3 - Atualizar produto")
print("4 - Deletar produto")
print(" ")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    
    #create
    nome_produto =input("Digite o nome do produto: ")
    valor = int(input("Digite o valor do produto: "))
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()# edita o banco de dados
    print(" ")
    print("Produto cadastrado com sucesso!")


elif opcao == 2:
    
    #read
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(" ")
    print("Lista de produtos:")
    print(" ")
    for x in resultado:
            print(x)



elif opcao == 3:
    #update
    nome_produto =input("Digite o nome do produto: ")
    valor = int(input("Digite o valor do produto: "))
    comando = f'UPDATE vendas SET valor = {valor} where nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()
    print(" ")
    print("Produto atualizado com sucesso!")

elif opcao == 4:
    #delete
    nome_produto =input("Digite o nome do produto: ")
    comando = f'DELETE from vendas where nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()
    print(" ")
    print("Produto Removido com sucesso!")





cursor.close()
conexao.close()