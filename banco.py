import mysql.connector
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

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

def pad_arrays_to_same_length(arr1, arr2):
    max_len = max(len(arr1), len(arr2))
    arr1_padded = np.pad(arr1, (0, max_len - len(arr1)), 'constant')
    arr2_padded = np.pad(arr2, (0, max_len - len(arr2)), 'constant')
    return arr1_padded, arr2_padded

def comparador(features2):
    """Compara a impressão digital passada com as do banco de dados."""
    conexao = None
    cursor = None
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        # Recupera todas as features do banco
        cursor.execute("SELECT id, nome, email, nivel_acesso, features FROM usuarios")
        resultados = cursor.fetchall()
        
        max_similarity = 0
        usuario_correspondente = None

        for user_id, nome, email, nivel_acesso, features_blob in resultados:
            # Convertendo as features do banco de string para array
            features1 = np.fromstring(features_blob.strip('[]'), sep=',', dtype=np.int32)
            
            # Padronizando tamanhos dos arrays
            features1_padded, features2_padded = pad_arrays_to_same_length(
                features1, np.array(features2)
            )
            
            # Reshape para 2D
            features1_padded = features1_padded.reshape(1, -1)
            features2_padded = features2_padded.reshape(1, -1)
            
            # Calculando similaridade
            similarity = cosine_similarity(features1_padded, features2_padded)[0, 0]
            
            # Verifica se a similaridade ultrapassa o limite
            if similarity > max_similarity:
                max_similarity = similarity
                usuario_correspondente = nome, email, nivel_acesso

        if max_similarity >= 0.999:
            return usuario_correspondente, max_similarity
        else:
            return None, "Nenhum usuário encontrado com similaridade suficiente."

    except mysql.connector.Error as erro:
        return None, str(erro)

    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
            conexao.close()