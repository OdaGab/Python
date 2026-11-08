import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conex:
    with closing(conex.cursor()) as cursor:
        cursor.execute("select * from agenda")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")