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
    This method check if this is new title
    :param title: get new title from web
    :return: true if this title is exist in database, false otherwise
    """
    return is_title_exist(title)


def article_sport5(url_page, title, desc, web, cat, date, time):
    """
    This method insert the new article
    :param url_page: The current url
    :param title: The current title
    :param desc: The current subtitle
    :param web: The chosen web site
    :param cat: The chosen category
    :param date: The date of the article
    :param time: The time of the article
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
    """
    This method given the first title in the web site
    :param content: The content of the given web site
    :param soup: The content of the given web site after func beautiful soup
    :param web: The chosen web site
    :param cat: The chosen category
    :return: Number that show if this is a new title and insert that to data base if necessary
    """
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
    """
    This method given the other titles in the web site
    :param content: The content of the given web site
    :param web: The chosen web site
    :param cat: The chosen category
    :return: Number that count the new articles and insert that to data base if necessary
    """
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
    """
    This method given the other titles in the web site
    :param soup: The content of the given web site after func beautiful soup
    :param web: The chosen web site
    :param cat: The chosen category
    :return: Number that count the new articles and insert that to data base if necessary
    """
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
    This method control of getting the article from this web site
    :param url_page: Url of the main web site
    :param web: The chosen web site
    :param cat: The chosen category
    :return: Number of all the title from current page
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
    """
    This method control update article of this web site
    :return: Number of new articles
    """
    count_new_article_all = 0
    print("Start.. update article in sport5")
    for league in all_league_sport5:
        count_new_article_all += get_all_titles_from_sport5(all_league_sport5[league], "sport5", league)
    print("Finish.. update article in sport5\n")
    return count_new_article_all
