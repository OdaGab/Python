import sqlite3

with sqlite3.connect("agenda.db") as conec:
    for registro in conec.execute("SELECT * FROM agenda"):
        print(f"Nome: {registro[0]} Telefone: {registro[1]}")