import sqlite3


def connect():
    global conn, cur
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()


def disconnect():
    cur.close()
    conn.close()


def create_table_word():
    connect()
    cur.execute('CREATE TABLE IF NOT EXISTS Word( WORD TEXT, TITLE TEXT, FREQ INTEGER, PRIMARY KEY("WORD","TITLE")) ')
    cur.execute('CREATE TABLE IF NOT EXISTS Article(WEB TEXT, CATEGORY TEXT,TITLE TEXT,DESCRIPTION TEXT, '
                'URL TEXT,TEXT_ARTICLE TEXT, PRIMARY KEY("WEB","CATEGORY","TITLE"))')
    disconnect()


def data_entry(dict, title):
    connect()
    try:
        for key, value in dict.items():
            cur.execute('INSERT INTO Word (WORD, TITLE, FREQ) VALUES (?, ?, ?)', (key, title, value))
        conn.commit()
        disconnect()
    except sqlite3.Error as e:
        print(e)


def insert_new_article(web_page, category_page, title_article, text_description, url_article, text_article):
    try:
        connect()
        cur.execute('INSERT INTO Article (WEB, CATEGORY, TITLE, DESCRIPTION, URL, TEXT_ARTICLE) '
                    'VALUES (?, ?, ?, ?, ?, ?)', (web_page, category_page, title_article, text_description,
                                               url_article, text_article))
        conn.commit()
        disconnect()
    except sqlite3.Error as e:
        print(e)


def search_titles(web_page, category_page, subject):
    connect()
    try:
        subject = "%"+subject+"%"
        cur.execute('SELECT TITLE FROM Article WHERE WEB = ? and CATEGORY = ? and TEXT_ARTICLE like ?', (web_page, category_page, subject, ))
        titles = cur.fetchall()
        disconnect()
        return titles

    except sqlite3.Error as e:
        print(e)


def search_article(title):
    connect()
    try:
        cur.execute('SELECT DESCRIPTION, URL, TEXT_ARTICLE FROM Article WHERE TITLE = ?', (title,))
        information = cur.fetchall()
        disconnect()
        return information

    except sqlite3.Error as e:
        print(e)


def is_title_exist(title): 
    connect()
    try:
        cur.execute('SELECT COUNT(*) FROM Article WHERE TITLE = ?', (title,))
        information = cur.fetchall()
        disconnect()
        if information[0][0] > 0:
            return False
        else:
            return True

    except sqlite3.Error as e:
        print(e)

create_table_word()

