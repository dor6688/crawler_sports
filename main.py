import re
import urllib.request
from tkinter import Tk
import handle_databases
import counter_word
from tkinter import *

import requests
from bs4 import BeautifulSoup


class gui:
    def __init__(self, root):
        topFrame = Frame(root)
        window_width = 300
        window_height = 370
        position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
        root.title("crawler_sport")
        root.geometry("300x370+{}+{}".format(position_right, position_down))
        root.resizable(0, 0)
        text_subject = Label(root, text="Subject:")
        self.subject_entry = Entry(root)
        button1 = Button(text="Sport5", fg='black', command=lambda: self.sport_five())
        button2 = Button(text="Sport1", fg='black', command=lambda: self.sport_one())
        button3 = Button(text="One", fg='black', command=lambda: self.one_sport())
        text_subject.grid(row=0, column=1)
        self.subject_entry.grid(row=1, column=1)
        button1.grid(row=2, column=0)
        button2.grid(row=2, column=1)
        button3.grid(row=2, column=2)
        self.text_status_label = Label(root, text="Status: ")
        self.status_text_string = StringVar()
        self.text_status = Label(root, textvariable=self.status_text_string, fg="blue")
        self.status_text_string.set("Ready to start")
        self.text_status_label.grid(row=3, column=0)
        self.text_status.grid(row=3, column=1)
        self.website = ''
        self.category = ''
        self.subject = ''

    def sport_five(self):
        self.website = "Sport5"
        self.subject = self.subject_entry.get()
        self.open_category_window()
        print("Sport5")

    def sport_one(self):
        self.website = "Sport1"
        self.subject = self.subject_entry.get()
        self.open_category_window()
        print("Sport1")

    def one_sport(self):
        self.website = "One"
        self.subject = self.subject_entry.get()
        self.open_category_window()
        print("One")

    def open_category_window(self):
        self.status_text_string.set("Loading...")
        self.text_status.config(fg="Red")
        category_window = Toplevel(root)
        window_width = 200
        window_height = 300
        position_right = int(category_window.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(category_window.winfo_screenheight() / 2 - window_height / 2)
        category_window.geometry("200x300+{}+{}".format(position_right, position_down))
        self.status_text_string.set("Working on category...")
        self.text_status.config(fg="Red")
        category_window.title("Category Window")
        sport_button1 = Button(category_window, text="Israeli Football", fg='black',
                               command=lambda: self.set_category("Israeli Football"))
        sport_button2 = Button(category_window, text="International Football", fg='black',
                               command=lambda: self.set_category("International Football"))
        sport_button3 = Button(category_window, text="Israeli Basketball", fg='black',
                               command=lambda: self.set_category("Israeli Basketball"))
        sport_button4 = Button(category_window, text="NBA Basketball", fg='black',
                               command=lambda: self.set_category("NBA Basketball"))
        sport_save_button = Button(category_window, text="Save", width="8",
                                   command=lambda: self.close_category_window(category_window))
        sport_button1.place(relx=0.5, rely=0.1, anchor=CENTER)
        sport_button2.place(relx=0.5, rely=0.2, anchor=CENTER)
        sport_button3.place(relx=0.5, rely=0.3, anchor=CENTER)
        sport_button4.place(relx=0.5, rely=0.4, anchor=CENTER)
        sport_save_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def set_category(self, category):
        self.category = category
        print(self.category)

    def close_category_window(self, window):
        window.destroy()
        self.status_text_string.set("The results coming...")
        self.text_status.config(fg="green")
        self.open_result_window()

    def open_result_window(self):
        result_window = Toplevel(root)
        window_width = 200
        window_height = 300
        position_right = int(result_window.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(result_window.winfo_screenheight() / 2 - window_height / 2)
        result_window.geometry("200x300+{}+{}".format(position_right, position_down))
        result_window.title("Your Results")

        result_window.resizable(0, 0)
        label_website = Label(result_window, text="Website:%s" % self.website)
        label_website.grid(row=0, column=1)
        label_category = Label(result_window, text="Category:%s" % self.category)
        label_category.grid(row=1, column=1)
        label_subject = Label(result_window, text="Subject:%s" % self.subject)
        label_subject.grid(row=2, column=1)
# subject.get give us the user query
# home_page = "https://www.sport5.co.il/"


israeli_football = "https://www.sport5.co.il/world.aspx?FolderID=4439&lang=he"
# world_football = "https://www.sport5.co.il/world.aspx?FolderID=4453&lang=he"
# israeli_basketball = "https://www.sport5.co.il/world.aspx?FolderID=4467&lang=he"
# nba = "https://nba.sport5.co.il/NBA.aspx?FolderId=402&lang=HE"


def get_all_titles_from_sport5(url, web="sport5", cat="israeli_footbal"):
    """
    :param url: get url page
    :return: all the title from current page
    """
    dic = {}
    source = requests.get(url).text
    soup = BeautifulSoup(source)
    content = soup.find('div', class_="content-block")
    first_url = content.find('a')['href']
    first_title = soup.find('div', class_="bomba-title").text
    first_description = soup.find('div', class_="bomba-subtitle").text
    article_sport5(first_url, first_title, web, cat)
    title = content.findAll('li')
    for con in title:
        if not con.find('h2') is None:
            title = con.find('h2').text
            link = con.find('h2').find('a')['href']
            dic[title] = link
            article_sport5(link, title, web, cat)

    content = soup.findAll('div', class_="text-holder")
    for con in content:
        if not con.find('h2') is None:
            title = con.find('h2').text
            link = con.find('h2').find('a')['href']
            dic[title] = link
            article_sport5(link, title, web, cat)


def article_sport5(url, title, web, cat):
    """
    :param url: current page
    :return: the word in the article
    """
    source = requests.get(url).text
    soup = BeautifulSoup(source)
    try:
        context = soup.find('div', id="find-article-content").text
        counter_word.start(context, title)
        handle_databases.insert_new_article(web, cat, title, url, context)
    except:
        print("Error !")


def article_sport1(param):
    """
        :param url: current page
        :return: the word in the article
    """
    lines = ""
    regex = '<div class="article-inner-content">(.+?)>'
    pattern = re.compile(regex)
    with urllib.request.urlopen(param) as response:
        html = response.read().decode('utf-8')
        print(html.find("<div class=\"article-inner-content\">"))
        print(html.find(" </div>"))
        tmp = html[html.find("<div class=\"article-inner-content\">"): html.find(" </div>")]
        article_lines = re.findall(pattern, html)
        for line in article_lines:
            lines += line
        # counter_word.start(lines)


def split_titles(titles):
    """
    :param titles: list with all url and title
    :return: transfer to article the url per article
    """
    for title in titles:
        title_split = title.split("target=\"_self")
        if len(title_split) > 1:
            article_sport5(str(title_split[0][1:len(title_split[0])-2]))
        #else:
            article_sport1(title[1:len(title)-1])





def get_all_titles_from_sport1(url):
    """
        :param url: get url page
        :return: all the title from current page
    """
    regex = '<a href=(.+?)>'  # split by this regex
    pattern = re.compile(regex)
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
    list_titles = re.findall(pattern, html)  # find all the title between the regex
    clear_list = []
    for title in list_titles:
        if title.startswith('"https://sport1.maariv.co.il'):
            clear_list.append(title)
    return clear_list


def get_article_from_url(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source)
    print(soup.find('div', id="find-article-content").text)


url = "https://www.sport5.co.il/"





#titles = get_all_titles_from_sport1(israeli_football)
titles = get_all_titles_from_sport5(israeli_football)
for url in titles:
    get_article_from_url(url)




root = Tk()
g = gui(root)
root.mainloop()
# split_titles(titles)

