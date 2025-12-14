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

cursor = conexao.cursor()
print("Banco conectado com sucesso!")

while True:
    print("\n" + "="*30)
    print("SISTEMA DE VENDAS")
    print("="*30)
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Atualizar produto")
    print("4 - Deletar produto")
    print("5 - Sair")
    print("="*30)

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        continue # Volta para o início do loop

    if opcao == 1:
        # Create
        nome_produto = input("Digite o nome do produto: ")
        valor = int(input("Digite o valor do produto: "))
        
        # Modo SEGURO com %s
        comando = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"
        valores = (nome_produto, valor)
        cursor.execute(comando, valores)
        conexao.commit()
        print(f"✅ Produto '{nome_produto}' cadastrado com sucesso!")

    elif opcao == 2:
        # Read
        comando = 'SELECT * FROM vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        print("\n--- Lista de produtos ---")
        for x in resultado:
            # x[0] é o ID (se tiver), x[1] nome, x[2] valor (depende da ordem da sua tabela)
            print(x) 

    elif opcao == 3:
        # Update
        nome_produto = input("Digite o nome do produto que deseja atualizar: ")
        novo_valor = int(input("Digite o NOVO valor do produto: "))
        
        # Modo SEGURO
        comando = "UPDATE vendas SET valor = %s WHERE nome_produto = %s"
        valores = (novo_valor, nome_produto)
        cursor.execute(comando, valores)
        conexao.commit()
        print("✅ Produto atualizado com sucesso!")

    elif opcao == 4:
        # Delete
        nome_produto = input("Digite o nome do produto para deletar: ")
        
        # Modo SEGURO
        comando = "DELETE FROM vendas WHERE nome_produto = %s"
        valores = (nome_produto,) # Precisa da vírgula pois é uma tupla de um item só
        cursor.execute(comando, valores)
        conexao.commit()
        print("✅ Produto removido com sucesso!")

    elif opcao == 5:
        print("Saindo do sistema...")
        break # Quebra o loop while e vai para o final do código

    else:
        print("❌ Opção inválida! Tente novamente.")

# Só fecha a conexão quando o usuário escolhe sair
cursor.close()
conexao.close()
print("Conexão encerrada.")