import sqlite3
conex = sqlite3.connect("agenda.db")
cursor = conex.cursor()
cursor.execute("select * from agenda")

while True:
    resultado = cursor.fetchone()
    if resultado is None:
        break

    print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")

cursor.close()
conex.close()