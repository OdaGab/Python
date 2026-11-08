"""
Lado bom
Esse código é ótimo para aprender o comando rowcount, porque mostra na prática quantas linhas foram afetadas por um UPDATE. É uma forma simples de entender que o banco responde com informação útil depois da execução.

Lado ruim
O problema é que esse exemplo pode passar a ideia de que rowcount resolve tudo sozinho. Na prática, ele pode ser 0 ou até -1 dependendo da operação, então sem entender o contexto pode gerar confusão. Além disso, sem WHERE, você pode alterar todos os registros por acidente.

Conclusão
É um exemplo didático muito bom para aprender rowcount, mas deve ser usado com cuidado, porque o comando ajuda a confirmar a operação, mas não substitui atenção ao código e ao uso correto do WHERE.


"""


import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conec:
    with closing(conec.cursor()) as cursor:
        cursor.execute(""" update agenda
                           set telefone = '1234-5678'""")
        print("Registros alterados: ", cursor.rowcount)

