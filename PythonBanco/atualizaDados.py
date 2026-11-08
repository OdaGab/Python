import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conec:
    with closing(conec.cursor()) as cursor:
        cursor.execute("""update agenda
                             set telefone = '91414-1721'
                            where nome = 'Odair'""" )
        conec.commit()