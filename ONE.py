from handle_databases import *
import requests
from bs4 import BeautifulSoup
import datetime

url = "https://www.one.co.il/"
israeli_football = "https://www.one.co.il/League/Current/1,0,0,0/%D7%9B%D7%93%D7%95%D7%A8%D7%92%D7%9C%20%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99"
world_football = "https://www.one.co.il/League/Current/3,0,0,0/%D7%9B%D7%93%D7%95%D7%A8%D7%92%D7%9C%20%D7%A2%D7%95%D7%9C%D7%9E%D7%99"
israeli_basketball = "https://www.one.co.il/League/Current/2,0,0,0/%D7%9B%D7%93%D7%95%D7%A8%D7%A1%D7%9C%20%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99"
nba = "https://www.one.co.il/League/Current/5,0,0,0/%D7%9B%D7%93%D7%95%D7%A8%D7%A1%D7%9C%20%D7%A2%D7%95%D7%9C%D7%9E%D7%99"

all_league_sport_one = {"israeli_football": israeli_football, "world_football": world_football,
              "israeli_basketball": israeli_basketball, "nba": nba}


def new_title(title):
    """
    This method check if this is new title
    :param title: get new title from web
    :return: true if this title is exist in database, false otherwise
    """
    return is_title_exist(title)


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
        first_url = url + content.find('a')['href'][1:]
        first_title = soup.find('div', id="LeagueTopArticle")
        title = first_title.find('h2', class_="marpad0").text.replace("\n", "").replace("\r", "").replace("  ", "")
        if new_title(title):
            desc = first_title.find('h3', class_="marpad0 f12").text.replace("\n", "").replace("\r", "").replace("  ",                                                                                                           "")
            print("Found new article in " + web + " category : " + cat)
            print("Main : " + title)
            article_sport_one(first_url, title, desc, web, cat)
            return 1
        else:
            return 0
    except:
        print("Error in first article")
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
    title = content.findAll('div', class_='EmptyClassArticleContainer')
    for con in title:
        if not con.find('h2') is None:
            # title
            title = con.find('h2').text.replace("\n", "").replace("\r", "").replace("  ", "")
            if new_title(title):
                # subTitle
                desc = con.find('h3').text.replace("\n", "").replace("\r", "").replace("  ", "")
                link = url + con.find('a')['href'][1:]
                print("Found new article in " + web + " category : " + cat)
                print(title)
                article_sport_one(link, title, desc, web, cat)
                count += 1
    return count


def get_all_titles_from_sport_one(url_page, web="one", cat="israeli_football"):
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
    content = soup.find('div', class_="blue")
    count_new_article += main_title(content, soup, web, cat)
    count_new_article += second_titles(content, web, cat)
    return count_new_article


def article_sport_one(url_page, title, desc, web, cat):
    """
    This method insert the new article
    :param url_page: The current url
    :param title: The current title
    :param desc: The current subtitle
    :param web: The chosen web site
    :param cat: The chosen category
    """
    context = ''
    source = requests.get(url_page).text
    soup = BeautifulSoup(source, features="html.parser")
    text_p = soup.findAll('p')
    for line in list(text_p):
        context += "".join(line.text)
        context += "".join("\n")

    try:
        post = soup.find('div', class_="article-credit").find('span').text
        split_post = post.split(" ")
        date = split_post[len(split_post) - 2]
        time = split_post[len(split_post) - 1]
        insert_new_article(web, cat, title, desc, url_page, context, date, time)
    except:
        now = datetime.datetime.now()
        date = str(now.date().strftime("%d/%m/%Y"))
        time = str(now.time())[:5]
        insert_new_article(web, cat, title, desc, url_page, context, date, time)


def update_articles():
    """
    This method control update article of this web site
    :return: Number of new articles
    """
    count_new_article_all = 0
    print("Start.. update article in one")
    for league in all_league_sport_one:
        count_new_article_all += get_all_titles_from_sport_one(all_league_sport_one[league], "one", league)
    print("Finish.. update article in one")
    return count_new_article_all
