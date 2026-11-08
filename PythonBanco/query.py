import sqlite3
conex = sqlite3.connect("agenda.db")
cursor = conex.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchall()

for registro in resultado:
    print(f"Nome: {registro[0]}\nTelefone: {registro[1]}")

cursor.close()
conex.close()

