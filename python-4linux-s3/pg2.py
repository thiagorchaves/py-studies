import psycopg2

try:
    con = psycopg2.connect(
        'host=localhost dbname=projeto user=thiago password=261009')
    cur = con.cursor()
except Exception as e:
    print("Erro: {}".format(e))
    exit()

cur.execute("insert into usuarios (nome, idade) values ('Izabel', 59);")
con.commit()

cur.execute("select * from usuarios")
con.commit()

cur.close()
con.close()

