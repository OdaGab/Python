import sqlite3 
from contextlib import closing

with sqlite3.connect("agenda.db") as conec:
    conec.row_factory = sqlite3.Row
    with closing(conec.cursor()) as cursor:
        for registro in cursor.execute("SELECT * FROM agenda"):
            print(f"Nome: {registro['nome']}Telefone: {registro['telefone']}")