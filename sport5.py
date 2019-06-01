from bs4 import BeautifulSoup
from handle_databases import *
import requests


sport5_url = "https://www.sport5.co.il/"
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


def article_sport5(url_page, title, desc, web, cat, date, time):
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
        insert_new_article(web, cat, title, desc, url_page, context, date, time)
    except:
        print("Error !  " + url_page)


def main_title(content, soup, web, cat):
    try:
        first_url = content.find('a')['href']
        if 'dayevents' not in first_url:
            first_title = soup.find('div', class_="content-block")
            title = first_title.find('div', class_="bomba-title").text
            if new_title(title):
                desc = first_title.find('div', class_="bomba-subtitle").text
                date_article = first_title.find('em', class_="date").text.replace(" ", "")
                date = date_article.split('-')[0]
                time = date_article.split('-')[1]
                print("Found new article in " + web + " category : " + cat)
                print("Main : " + title + " " + desc)
                article_sport5(first_url, title, desc, web, cat, date, time)
                return 1
            else:
                return 0
        else:
            print(first_url)
            return 0
    except:
        try:
            first_title = soup.find('div', class_="desc")
            title = first_title.find('h2', class_="title").text
            if new_title(title):
                desc = first_title.find('p', class_="h3").text
                date_article = first_title.find('em', class_="date").text.replace(" ", "")
                date = date_article.split('-')[0]
                time = date_article.split('-')[1]
                print("Found new article in " + web + " category : " + cat)
                print("Main : " + title + " " + desc)
                article_sport5(first_url, title, desc, web, cat, date, time)
                return 1
            else:
                return 0
        except:
            print("Error in first article ")
            return 0


def second_titles(content, web, cat):
    count = 0
    titles = content.findAll('li')
    for current_title in titles:
        if not current_title.find('h2') is None:
            title_page = current_title.find('h2').text
            if new_title(title_page):
                link_page = current_title.find('h2').find('a')['href']
                if 'dayevents' not in link_page:
                    desc_page = current_title.find('p', class_="abstract").text
                    date_article = current_title.find('em', class_="date").text.replace(" ", "")
                    date = date_article.split('-')[0]
                    time = date_article.split('-')[1]
                    print("Found new article in " + web + " category : " + cat)
                    print(title_page + " " + desc_page)
                    article_sport5(link_page, title_page, desc_page, web, cat, date, time)
                    count += 1
    return count


def third_titles(soup, web, cat):
    count = 0
    content = soup.findAll('div', class_="text-holder")
    for con in content:
        if not con.find('h2') is None:
            title = con.find('h2').text
            if new_title(title):
                link = con.find('h2').find('a')['href']
                if 'dayevents' not in link and 'sport' in link:
                    desc = con.find('p').text
                    date_article = con.find('em', class_="date").text.replace(" ", "").replace("\n", "").replace("\r", "")
                    date = date_article.split('-')[0][-8:]
                    time = date_article.split('-')[1]
                    print("Found new article in " + web + " category : " + cat)
                    print(title + " " + desc)
                    article_sport5(link, title, desc, web, cat, date, time)
                    count += 1
    return count


def get_all_titles_from_sport5(url_page, web="sport5", cat="israeli_football"):
    """
    :param url_page: get url page
    :param web: which web
    :param cat: sports category
    :return: all the title from current page
    """
    count_new_article = 0
    source = requests.get(url_page).text
    soup = BeautifulSoup(source, features="html.parser")
    content = soup.find('div', class_="content-block")
    count_new_article += main_title(content, soup, web, cat)
    count_new_article += second_titles(content, web, cat)
    count_new_article += third_titles(soup, web, cat)
    return count_new_article


def update_articles():
    count_new_article_all = 0
    print("Start.. update article in sport5")
    for league in all_league_sport5:
        count_new_article_all += get_all_titles_from_sport5(all_league_sport5[league], "sport5", league)
    print("Finish.. update article in sport5\n")
    return count_new_article_all



