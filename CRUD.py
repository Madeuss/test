import MySQLdb

host = "localhost"
user = "dev"
password = "devel@2020"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):

    global c

    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where
    
    c.execute(query)

    return c.fetchall()

#result = select("name, district", "city", "population > 5000000")
#print(result[0]["name"]) 
# ou 
#print(select("name, continent", "country" ))

def insert(values, table, fields=None):
    global c, con

    query = "INSERT INTO " + table
    if(fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    c.execute(query)
    con.commit() 
    return c.fetchall()

#values = ["DEFAULT, 'Ronaldo', '2000-01-01', '47852364418', '5388777451'"]->exemplo
#insert(values, "table_name", fields_se_tiver)->insert padrão
#insert(values, "aluno")->exemplo!
#print(select("*","aluno"))


def update(sets, table, where=None):

    global c, con

    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if (where):
        query = query + " WHERE " + where

    print(query)
    c.execute(query)
    con.commit() 
    return c.fetchall()

#update({"nome":"Mateus", "data_nasc":"2000-03-24"}, "aluno", "idaluno = 1")
#print(select("*", "aluno"))

def delete(table, where):

    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()
    return c.fetchall()

#delete("aluno","idaluno = 2")
#print(select("*", "aluno"))
