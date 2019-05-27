import urllib.request
from handle_databases import *
import counter_word
from tkinter import *
import requests
from bs4 import BeautifulSoup
import threading


url = "https://www.sport5.co.il/"
israeli_football = "https://www.sport5.co.il/world.aspx?FolderID=4439&lang=he"
world_football = "https://www.sport5.co.il/world.aspx?FolderID=4453&lang=he"
israeli_basketball = "https://www.sport5.co.il/world.aspx?FolderID=4467&lang=he"
nba = "https://nba.sport5.co.il/NBA.aspx?FolderId=402&lang=HE"

all_league_sport5 = {"israeli_football": israeli_football, "world_football": world_football,
              "israeli_basketball": israeli_basketball, "nba": nba}


def new_title(title):
    """
    :param title: get new title from web
    :return: true if this title is exist in database, false otherwise
    """
    return is_title_exist(title)


def get_all_titles_from_sport5(url_page, web="sport5", cat="israeli_football"):
    """
    :param url_page: get url page
    :param web: which web
    :param cat: sports category
    :return: all the title from current page
    """
    dic = {}
    source = requests.get(url_page).text
    soup = BeautifulSoup(source, features="html.parser")
    content = soup.find('div', class_="content-block")
    try:
        first_url = content.find('a')['href']
        first_title = soup.find('div', class_="content-block")
        title = first_title.find('div', class_="bomba-title").text
        if new_title(title):
            desc = first_title.find('div', class_="bomba-subtitle").text
            print("Main : " + title + " " + desc)
            article_sport5(first_url, title, desc, web, cat)
    except:
        try:
            first_title = soup.find('div', class_="desc")
            title = first_title.find('h2', class_="title").text
            if new_title(title):
                desc = first_title.find('p', class_="h3").text
                print("Main : " + title + " " + desc)
                article_sport5(first_url, title, desc, web, cat)
        except:
            print("Error in first article")

    title = content.findAll('li')
    for con in title:
        if not con.find('h2') is None:
            title = con.find('h2').text
            if new_title(title):
                desc = con.find('p', class_="abstract").text
                link = con.find('h2').find('a')['href']
                dic[title] = link
                print(title + " " + desc)
                article_sport5(link, title, desc, web, cat)

    content = soup.findAll('div', class_="text-holder")
    for con in content:
        if not con.find('h2') is None:
            title = con.find('h2').text
            if new_title(title):
                desc = con.find('p').text
                link = con.find('h2').find('a')['href']
                dic[title] = link
                print(title + " " + desc)
                article_sport5(link, title, desc, web, cat)


def article_sport5(url_page, title, desc, web, cat):
    """
    :param url_page: current page
    :param title: title of article
    :param desc: description of article
    :param web: web of the article
    :param cat: category of the article
    :return: the word in the article
    """
    source = requests.get(url_page).text
    soup = BeautifulSoup(source, features="html.parser")
    try:
        if 'play' in url_page:
            context = soup.find('div', class_="article-content").text
        else:
            context = soup.find('div', id="find-article-content").text
        counter_word.start(context, title)
        insert_new_article(web, cat, title, desc, url_page, context)
    except:
        print("Error !  " + url_page)


# itay here
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


# itay here
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

'''
def split_titles(titles):
    """
    :param titles: list with all url and title
    :return: transfer to article the url per article
    """
    for title in titles:
        title_split = title.split("target=\"_self")
        if len(title_split) > 1:
            article_sport5(str(title_split[0][1:len(title_split[0]) - 2]))
            # else:
            article_sport1(title[1:len(title) - 1])


def get_article_from_url(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, features="html.parser")
    print(soup.find('div', id="find-article-content").text)
'''




def update_articles():
    print("Start.. update article")
    threading.Timer(60.0, update_articles).start()
    for league in all_league_sport5:
        print(league)
        get_all_titles_from_sport5(all_league_sport5[league], "sport5", league)
    print("Finish.. update article")

update_articles()