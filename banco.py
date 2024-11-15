import mysql.connector
from pathlib import Path

def obter_conexao():
    """Estabelece e retorna a conexão com o banco de dados."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="digital123",
        database="banco"
    )

def cadastrar_usuario(nome, email, nivel_acesso, features):
    """Cadastra um usuário no banco de dados."""
    
    conexao = None
    cursor = None
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        query = """
        INSERT INTO usuarios (nome, email, nivel_acesso, features)
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(query, (nome, email, nivel_acesso, str(features)))
        conexao.commit()
        
        return True, "Cadastro realizado com sucesso!"

    except mysql.connector.Error as erro:
        return False, str(erro)

    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()

def buscar_usuario_por_impressao_digital(caminho_imagem):
    """Busca um usuário no banco de dados pela impressão digital."""
    conexao = None
    cursor = None

    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT nome FROM usuarios WHERE impressao_digital = %s", (caminho_imagem,))
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0], None  # Retorna o nome do usuário e None para mensagem de erro
        else:
            return None, "Nenhum usuário encontrado para essa impressão digital."

    except mysql.connector.Error as err:
        return None, str(err)

    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()
