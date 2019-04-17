import sqlite3

conn = sqlite3.connect('web_database.db')
c = conn.cursor()


def create_table():
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Website( WEBSITE TEXT, CATEGORY TEXT, TITLES TEXT, CONTENT TEXT)')
    c.close()
    conn.close()


def data_entry():
    c.execute("INSERT INTO Website(WEBSITE, CATEGORY, TITLES, CONTENT) VALUES ('sport5', 'NBA', 'dor','number 1')")
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()
