import sqlite3
dados = [("Tatisa", "91234-4321"),
         ("Johann", "97890-0987"),
         ("Liam",   "98765-5678"),
         ("Odair",  "91414-1721")]

conex =sqlite3.connect("agenda.db")
cursor = conex.cursor()
cursor.executemany('''
                    insert into agenda(nome, telefone)
                    values(?,?)
                    ''', dados)
conex.commit()
cursor.close()
conex.close()