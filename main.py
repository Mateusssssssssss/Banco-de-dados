import sqlite3
from pathlib import Path

from numpy import insert

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

#registrar valores nas colunas das tabelas / modo correto
#prevenindo sql inject

insert_into = (f'INSERT INTO {TABLE_NAME} (name, weigth)'
               'VALUES (?, ?)'
               ) 
#execute para passar um valor e 
cursor.execute(insert_into,['Joana', 4])
#executemany para passar varios valores!
cursor.executemany(insert_into,[['Joana', 4], ['Mateus', 10], ['Lucenia', 8]])

connection.commit()

#fechar as conexões
cursor.close(),
connection.close()