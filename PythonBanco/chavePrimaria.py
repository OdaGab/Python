import sqlite3
from contextlib import closing

dados = [["Odair Gabriel", 40], ["Liam Gabriel", 10], ["Johann Gabriel", 15], ["Tatisa França", 30]]

with sqlite3.connect("pacientes.db") as conec:
    conec.row_factory = sqlite3.Row
    with closing(conec.cursor()) as cursor:
        cursor.execute("""create table pac (
        id integer primary key autoincrement,
        nome text,
        idade integer)""")

        cursor.executemany("insert into pac(nome, idade) values(?,?)", dados)
        conec.commit()