import sqlite3

connection = sqlite3.connect("word_database.db")
cursor = connection.cursor()

word_sql = ''' CREATE TABLE IF NOT EXISTS Word
                         ( WORD VARCHAR,
                         APPEARANCE INT,
                         WEB )'''
cursor.execute(word_sql)
insert = "INSERT INTO Word (WORD , APPEARANCE, WEB) VALUES ('dor',5,'Sfsfdsf')"
cursor.execute(insert)
