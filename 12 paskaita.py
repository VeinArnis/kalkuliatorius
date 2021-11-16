import sqlite3

conn = sqlite3.connect("paskaita6.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS CodeAcademy (
            pavadinimas text,
            destytojas text,
            trukme integer
            )""")

with conn:
    c.execute("INSERT INTO CodeAcademy VALUES ('Vadyba', 'Domantas', '40')")
    c.execute("INSERT INTO CodeAcademy VALUES ('Python', 'Donatas', '80')")
    c.execute("INSERT INTO CodeAcademy VALUES ('Java', 'Tomas', '80')")
    c.execute("UPDATE CodeAcademy SET pavadinimas = 'Python programavimas' WHERE destytojas='Donatas' ")
    c.execute("DELETE from CodeAcademy WHERE destytojas = 'Tomas' ")

with conn:
    c.execute("SELECT * FROM CodeAcademy")
    print(c.fetchall())

with conn:
    c.execute("SELECT * FROM CodeAcademy WHERE trukme > '50' ")

conn.commit()
conn.close()
