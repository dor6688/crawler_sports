from bs4 import BeautifulSoup
from handle_databases import *
from collections import Counter


def start(text, title):
    soup = BeautifulSoup(text, features="html.parser")
    content = soup.text
    clean_text = clean_symbols(content)
    create_dictionary(clean_text, title)


def clean_symbols(text):
    symbols = "!@#$%^&*(){}[]\"<>?/'.;`_=+-:|,"
    for char in symbols:
        text = text.replace(char, "")
    text = text.replace('\n', " ")
    return clean_stop_words(text)


def clean_stop_words(text):
    stop_words = ["", '', "לא", "את", "של", "עם", "הוא", "היא", "זה", "אבל", "אני", "יש", "כל", "רק", "בין", "מי",
                  "הייתי", "איך", "עוד", "על", "ללא", "אלא", "גם", "או", "שלי", "מה", "היה", "הם", "אם", "אנחנו", "אחרי"]
    words = text.split(" ")
    clean_stop = list(filter(lambda current_word: not stop_words.__contains__(current_word), words))
    return clean_stop


def create_dictionary(cleaned_word_list, title):
    word_count = Counter(cleaned_word_list)
    data_entry(word_count, title)
