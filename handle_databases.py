import sqlite3


def connect():
    """
    This method control of the connect to the database
    """
    global conn, cur
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()


def disconnect():
    """
    This method control of the disconnect from the database
    """
    cur.close()
    conn.close()


def create_table_word():
    """
    This method create the table words
    """
    connect()
    cur.execute('CREATE TABLE IF NOT EXISTS Article(WEB TEXT, CATEGORY TEXT,TITLE TEXT,DESCRIPTION TEXT, URL TEXT,'
                'TEXT_ARTICLE TEXT, DATE_ARTICLE TEXT, TIME_ARTICLE TEXT, PRIMARY KEY("WEB","CATEGORY","TITLE"))')
    disconnect()


def data_entry(dictionary, title):
    """
    This method insert word to the table
    :param dictionary: Word dictionary
    :param title: The chosen title
    """
    connect()
    try:
        for key, value in dictionary.items():
            cur.execute('INSERT INTO Word (WORD, TITLE, FREQ) VALUES (?, ?, ?)', (key, title, value))
        conn.commit()
        disconnect()
    except sqlite3.Error as e:
        print(e)


def insert_new_article(web_page, category_page, title_article, text_description, url_article, text_article,
                       date_article, time_article):
    """
    This method insert new article to the table article
    :param web_page: The web site of the new article
    :param category_page: The category of the new article
    :param title_article: The title of the new article
    :param text_description: The subtitle of the new article
    :param url_article: The url of the new article
    :param text_article: The text of the new article
    :param date_article: The date of the new article
    :param time_article: The time of the new article
    """
    try:
        connect()
        cur.execute('INSERT INTO Article (WEB, CATEGORY, TITLE, DESCRIPTION, URL, TEXT_ARTICLE, DATE_ARTICLE, TIME_ARTICLE) '
                    'VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (web_page, category_page, title_article, text_description,
                    url_article, text_article, date_article, time_article))
        conn.commit()
        disconnect()
    except sqlite3.Error as e:
        print(e)


def search_titles(web_page, category_page, subject):
    """
    This method search title from database
    :param web_page: The chosen web site
    :param category_page: The chosen category
    :param subject: The chosen word subject
    :return: The relevant titles for the given params
    """
    connect()
    try:
        subject = "%"+subject+"%"
        cur.execute('SELECT TITLE FROM Article WHERE WEB = ? and CATEGORY = ? and (TEXT_ARTICLE like ? or TITLE like ?'
                    'or DESCRIPTION like ?) '
                    ' ORDER BY date_article DESC, time_article DESC ', (web_page, category_page, subject, subject, subject))
        titles = cur.fetchall()
        disconnect()
        return titles

    except sqlite3.Error as e:
        print(e)


def get_all_articles_cat(web, cat):
    """
    This method control of article with chosen web site and chosen category
    :param web: The chosen web site
    :param cat: The chosen category
    :return: The relevant titles for the given params
    """
    connect()
    try:
        cur.execute(
            'SELECT TEXT_ARTICLE FROM Article WHERE WEB = ? and CATEGORY = ?', (web, cat,))
        titles = cur.fetchall()
        disconnect()
        return titles

    except sqlite3.Error as e:
        print(e)


def search_article(title):
    """
    This method gives the information of chosen title
    :param title: The chosen title
    :return: The information for this title
    """
    connect()
    try:
        cur.execute('SELECT DESCRIPTION, URL, TEXT_ARTICLE FROM Article WHERE TITLE = ?', (title,))
        information = cur.fetchall()
        disconnect()
        return information

    except sqlite3.Error as e:
        print(e)


def is_title_exist(title):
    """
    This method check if the title exist in the data base
    :param title: Agiven title
    :return: Boolean answer - true if exist and false if is a new title
    """
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

