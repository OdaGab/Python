import sqlite3

with sqlite3.connect("pacientes.db") as conec:
    conec.row_factory = sqlite3.Row
    print(f"{'Id':4s}{'Nome':<20s} {'Idade':10s}")
    print("=" * 35)
    for nome in conec.execute("select * from pac order by nome"):
        print(f"{nome['id']:3d} {nome['nome']:<20s} {nome['idade']}")