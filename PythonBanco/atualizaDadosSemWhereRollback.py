
import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conec:
    with closing(conec.cursor()) as cursor:
        cursor.execute(""" update agenda
                           set telefone = '1234-5670'""")
        print("Registros que a serem atualizador: ", cursor.rowcount)

        if cursor.rowcount == 1:
            conec.commit()
            print("Alterações Gravadas")
        else:
            conec.rollback()
            print("Alteração Abortadas")

"""
Sim, esse tipo de exemplo é útil para ensinar rowcount, mas:

É didático demonstra o conceito não é o ideal para uso real sem WHERE

"""

