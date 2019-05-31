import urllib.request
from handle_databases import *
from tkinter import *
import requests
from bs4 import BeautifulSoup

url = "https://www.one.co.il/"
israeli_football = "https://www.one.co.il/League/Current/1,0,0,0/%D7%9B%D7%93%D7%95%D7%A8%D7%92%D7%9C%20%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99"
world_football = "https://www.one.co.il/League/Current/3,0,0,0/%D7%9B%D7%93%D7%95%D7%A8%D7%92%D7%9C%20%D7%A2%D7%95%D7%9C%D7%9E%D7%99"
israeli_basketball = "https://www.one.co.il/League/Current/2,0,0,0/%D7%9B%D7%93%D7%95%D7%A8%D7%A1%D7%9C%20%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99"
nba = "https://www.one.co.il/League/Current/5,0,0,0/%D7%9B%D7%93%D7%95%D7%A8%D7%A1%D7%9C%20%D7%A2%D7%95%D7%9C%D7%9E%D7%99"

all_league_sport_one = {"israeli_football": israeli_football, "world_football": world_football,
              "israeli_basketball": israeli_basketball, "nba": nba}


def new_title(title):
    """
    :param title: get new title from web
    :return: true if this title is exist in database, false otherwise
    """
    return is_title_exist(title)


def get_all_titles_from_sport_one(url_page, web="sport5", cat="israeli_football"):
    """
    :param url_page: get url page
    :param web: which web
    :param cat: sports category
    :return: all the title from current page
    """
    dic = {}
    source = requests.get(url_page).text
    soup = BeautifulSoup(source, features="html.parser")
    content = soup.find('div', class_="blue")
    try:
        first_url = url + content.find('a')['href'][1:]
        first_title = soup.find('div', id="LeagueTopArticle")
        title = first_title.find('h2', class_="marpad0").text.replace("\n", "").replace("\r", "").replace("  ", "")
        if new_title(title):
            desc = first_title.find('h3', class_="marpad0 f12").text.replace("\n", "").replace("\r", "").replace("  ", "")
            print("Found new article in " + web + " category : " + cat)
            print("Main : " + title + " " + desc)
            article_sport_one(first_url, title, desc, web, cat)
    except:
        print("Error in first article")

    title = content.findAll('div', class_='EmptyClassArticleContainer')
    for con in title:
        if not con.find('h2') is None:
            # title
            title = con.find('h2').text.replace("\n", "").replace("\r", "").replace("  ", "")
            if new_title(title):
                # subTitle
                desc = con.find('h3').text.replace("\n", "").replace("\r", "").replace("  ", "")
                link = url + con.find('a')['href'][1:]
                dic[title] = link
                print("Found new article in " + web + " category : " + cat)
                print(title + " " + desc)
                article_sport_one(link, title, desc, web, cat)


def article_sport_one(url_page, title, desc, web, cat):
    """
    :param url_page: current page
    :param title: title of article
    :param desc: description of article
    :param web: web of the article
    :param cat: category of the article
    :return: the word in the article
    """
    context = ''
    source = requests.get(url_page).text
    soup = BeautifulSoup(source, features="html.parser")
    text_p = soup.findAll('p')
    for line in list(text_p):
        try:
            context += "".join(line.text)
            context += "".join("\n")
        except Exception as e:
            print(e)
            continue
    try:
        post = soup.find('div', class_="article-credit").find('span').text
        split_post = post.split(" ")
        date = split_post[len(split_post) - 2]
        time = split_post[len(split_post) - 1]
        #counter_word.start(context, title)
        insert_new_article(web, cat, title, desc, url_page, context, date, time)
    except:
        print("Error !  " + url_page)


def update_articles():
    print("Start.. update article in one")
    for league in all_league_sport_one:
        get_all_titles_from_sport_one(all_league_sport_one[league], "one", league)
    print("Finish.. update article in one")
