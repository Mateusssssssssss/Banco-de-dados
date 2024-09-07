from os import name
import sqlite3
from main import DB_FILE, TABLE_NAME
connection = sqlite3.connect(DB_FILE)
#CURSOR é ele quem fará as consultas no banco de dados
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    _id, name, weigth = row
    print(_id, name, weigth)


#fechar as conexões
cursor.close(),
connection.close()