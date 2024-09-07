import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
#arquivo a ser usado DB_FILE
DB_FILE = ROOT_DIR / DB_NAME
#tabelas de nome
TABLE_NAME = 'customers'

#Conexão, DB_FILE arquivo a ser usado
connection = sqlite3.connect(DB_FILE)
#CURSOR é ele quem fará as consultas no banco de dados
cursor = connection.cursor() 

#criação de tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weigth REAL'
    ')'
    )
#executar o codigo
connection.commit()

#fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')

connection.commit()

#registrar valores nas colunas das tabelas
cursor.execute(f'INSERT INTO {TABLE_NAME} (id, name, weigth)'
               'VALUES ( NULL, "Lucenia", 10), (NULL, "Silvia", 9.9)'
               ) 

connection.commit()

#fechar as conexões
cursor.close(),
connection.close()