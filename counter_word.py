import requests
from bs4 import BeautifulSoup
import operator
import create_databases
import database_web

word_count = {}


def start(text):
    word_list = []
    soup = BeautifulSoup(text)
    content = soup.text
    words = content.split(" ")
    for each_word in words:
        word_list.append(each_word)
    clean_up(word_list)


def clean_up(word_list):
    cleaned_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*(){}[]\"<>?/'.;`_=+-:|,"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            cleaned_word_list.append(word)
    create_dictionary(cleaned_word_list)


def create_dictionary(cleaned_word_list):
    global word_count
    for word in cleaned_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in sorted(word_count.items(), key=operator.itemgetter(1), reverse=True):
        print(key, value)


start("צצכק חעח חעח חעח חלחל חלל חלל חלל חלל ממ מי מו מה")
create_databases.create_table()
create_databases.data_entry(word_count)
