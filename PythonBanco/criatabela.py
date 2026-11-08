import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute('''
               create table agenda(
               nome text,
               telefone text)
               ''')



conexao.commit()
cursor.close()
conexao.close()
