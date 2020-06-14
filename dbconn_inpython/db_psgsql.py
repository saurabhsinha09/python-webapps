# Details to be modified as per the postgress installation #
# database = either create db1 or use own name             #
# password = installation password                         #
# host = It can be local or any server                     #

import psycopg2

def create_table():
    conn = psycopg2.connect(database="db1", user="postgres", password="oracle", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    #cur.execute("INSERT INTO store VALUES ('Bat' , 10, 500)")
    conn.commit()
    conn.close()

create_table()

def insert_table(item, quantity, price):
    conn = psycopg2.connect(database="db1", user="postgres", password="oracle", host="localhost", port="5432")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close() 

#insert_table("Ball", 20, 50)
#insert_table("Wicket", 20, 75)

def select_table():
    conn = psycopg2.connect(database="db1", user="postgres", password="oracle", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_table(item):
    conn = psycopg2.connect(database="db1", user="postgres", password="oracle", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s",(item,))
    conn.commit()
    conn.close()     

#delete_table("Ball")

def update_table(quantity, price, item):
    conn = psycopg2.connect(database="db1", user="postgres", password="oracle", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",(quantity, price, item))
    conn.commit()
    conn.close() 

update_table(15, 550, "Ball")    
update_table(25, 500, "Wicket")

print(select_table())    