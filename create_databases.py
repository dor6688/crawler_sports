import sqlite3

conn = sqlite3.connect('word_database.db')
c = conn.cursor()


def create_table():
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Word( WORD TEXT, WEB TEXT)')
    c.close()
    conn.close()

def data_entry(word_dict):
    for word in word_dict:
        c.execute("INSERT INTO Word (WORD , WEB) VALUES (word, word_dict[word])")
        conn.commit()
    c.close()
    conn.close()


create_table()
data_entry(word_dict={})
