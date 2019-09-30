import MySQLdb

try:
    con = MySQLdb.connect(host='localhost', user='root',
        passwd='', db='projetos')
    cur = con.cursor()
except Exception as e:
    print('Erro: {}'.format(e))
    exit()
# cur.execute("insert into usuarios (nome, idade) values ('Matheus', 9);")
# cur.execute("update usuarios idade=32 where id=1")
# cur.execute("delete usuarios where id=1")
con.commit()

cur.execute("select * from usuarios")
# print(cur.fetchone())
print(cur.fetchall())

cur.close()
con.close()
