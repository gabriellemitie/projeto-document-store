import psycopg2  # ou use 'psycopg' se for a nova versão
import pymongo
from decimal import Decimal

def convert_decimal(data):
    if isinstance(data, dict):  # Se for um dicionário (linha da tabela)
        for key, value in data.items():
            if isinstance(value, Decimal):
                data[key] = float(value)  # Converte Decimal para float
    return data


def connect_postgres():
    try:
        conn = psycopg2.connect('postgresql://postgres:dificil@localhost:5432/projetobd3') 
        print("Conexão com PostgreSQL estabelecida com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro na conexão com PostgreSQL: {e}")
        return None

def connect_mongo():
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['document-store']  # Escolha o nome do banco de dados do MongoDB
        print("Conexão com MongoDB estabelecida com sucesso!")
        return db
    except Exception as e:
        print(f"Erro na conexão com MongoDB: {e}")
        return None

def migrate_all_tables():
    # Conectar ao PostgreSQL e ao MongoDB
    postgres_conn = connect_postgres()
    mongo_db = connect_mongo()

    if postgres_conn is None or mongo_db is None:
        print("Falha na conexão com os bancos de dados.")
        return

    try:
        # Listar todas as tabelas no banco de dados PostgreSQL
        cursor = postgres_conn.cursor()
        cursor.execute("""
            SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
        tables = cursor.fetchall()

        # Iterar sobre cada tabela e migrar os dados para o MongoDB
        for (table_name,) in tables:
            print(f"Migrando dados da tabela '{table_name}' para o MongoDB...")

            # Obter dados da tabela atual
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]

            # Criar uma coleção com o nome da tabela no MongoDB
            collection = mongo_db[table_name]

            # Inserir cada linha como um documento na coleção
            documents = [
                convert_decimal({column_names[i]: row[i] for i in range(len(column_names))})
                for row in rows
            ]
            if documents:
                collection.insert_many(documents)
                print(f"{len(documents)} registros migrados para a coleção '{table_name}' no MongoDB.")
            else:
                print(f"Nenhum dado encontrado na tabela '{table_name}'.")

    except Exception as e:
        print(f"Erro na migração de dados: {e}")
    
    finally:
        # Fechar as conexões
        cursor.close()
        postgres_conn.close()

# Executar a migração
migrate_all_tables()
