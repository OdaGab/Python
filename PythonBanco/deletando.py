import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conec:
    with closing(conec.cursor()) as cursor:
        cursor.execute("""delete from agenda where nome='Liam'""")
        print ("REGISTROS APAGADOS: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conec.commit()
            print("Alterações realizadas com sucesso!")
        else:
            conec.rollback()
            print("Alterações Abortadas")
