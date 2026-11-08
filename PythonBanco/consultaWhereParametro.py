import sqlite3
from contextlib import closing

#strip() - remove espaços vazios no começo e no fim de uma string.

nom = input("Digite o nome:").strip()

with sqlite3.connect("agenda.db") as conec:
    with closing(conec.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = ?", (nom,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print("Nada encontrado")
                break
            print(f"Nome: {resultado[0]} - Telefone: {resultado[1]}")
            x += 1