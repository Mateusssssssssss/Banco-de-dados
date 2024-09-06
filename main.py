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


#fechar as conexões
cursor.close(),
connection.close()