import requests
from bs4 import BeautifulSoup
import operator
import handle_databases
#import database_web

word_count = {}


def start(text, title):
    word_list = []
    soup = BeautifulSoup(text)
    content = soup.text
    words = content.split(" ")
    for each_word in words:
        word_list.append(each_word)
    clean_up(word_list, title)


def clean_up(word_list, title):
    cleaned_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*(){}[]\"<>?/'.;`_=+-:|,"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            cleaned_word_list.append(word)
    create_dictionary(cleaned_word_list, title)


def create_dictionary(cleaned_word_list, title):
    global word_count
    for word in cleaned_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in sorted(word_count.items(), key=operator.itemgetter(1), reverse=True):
        handle_databases.data_entry(key, title, value)




#start("צצכק חעח חעח חעח חלחל חלל חלל חלל חלל ממ מי מו מה")
#create_databases.create_table()
#create_databases.data_entry(word_count)


