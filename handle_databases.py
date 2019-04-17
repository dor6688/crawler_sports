import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


def create_table_word():
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Word( WORD TEXT, TITLE TEXT, FREQ INTEGER, PRIMARY KEY("WORD"), '
              'FOREIGN KEY("TITLE") REFERENCES "Article"("TITLE"))')
    c.execute('CREATE TABLE IF NOT EXISTS Article(WEB TEXT, CATEGORY TEXT,TITLE TEXT,URL TEXT,TEXT_ARTICLE TEXT, '
              'PRIMARY KEY("WEB","CATEGORY","TITLE"))')
    c.close()
    conn.close()


def data_entry(word, title, freq):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO Word (WORD, TITLE, FREQ) VALUES (?, ?, ?)', (word, title, freq))
    conn.commit()
    c.close()
    conn.close()


def insert_new_article(web_page, category_page, title_article, url_article, text_article):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO Article (WEB, CATEGORY, TITLE, URL, TEXT_ARTICLE) VALUES (?, ?, ?, ?, ?)',
              (web_page, category_page, title_article, url_article, text_article))
    conn.commit()
    c.close()
    conn.close()


create_table_word()

try:
    data_entry("dafa", "ADf", 6)

except:
    print("already exist")
