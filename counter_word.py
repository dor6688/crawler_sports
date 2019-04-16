import requests
from bs4 import BeautifulSoup
import operator


def start(text):
    word_list = []
    soup = BeautifulSoup(text)
    content = soup.string
    words = content.lower().split()
    for each_word in words:
        word_list.append(each_word)
    clean_up(word_list)


def clean_up(word_list):
    cleaned_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*(){}[]\"<>?/'.;`_=+-:|"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            cleaned_word_list.append(word)
    create_dictionary(cleaned_word_list)


def create_dictionary(cleaned_word_list):
    word_count = {}
    for word in cleaned_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


print("done")
