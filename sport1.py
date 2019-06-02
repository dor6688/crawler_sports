from handle_databases import *
import requests
from bs4 import BeautifulSoup


url = "https://sport1.maariv.co.il/"
israeli_football = "https://sport1.maariv.co.il/israeli-soccer"
world_football = "https://sport1.maariv.co.il/World-football"
israeli_basketball = "https://sport1.maariv.co.il/basketball/Winner-Basketball-League"
nba = "https://sport1.maariv.co.il/basketball/NBA"

all_league_sport1 = {"israeli_football": israeli_football, "world_football": world_football,
              "israeli_basketball": israeli_basketball, "nba": nba}


def new_title(title):
    """
    This method check if this is new title
    :param title: get new title from web
    :return: true if this title is exist in database, false otherwise
    """
    return is_title_exist(title)


def second_titles(content, web, cat):
    """
    This method given the other titles in the web site
    :param content: The content of the given web site
    :param web: The chosen web site
    :param cat: The chosen category
    :return: Number that count the new articles and insert that to data base if necessary
    """
    count = 0
    title = content.findAll('div', class_='col-xs-8 category-article-content')
    for con in title:
        if not con.find('span', class_='list-article-item-title').text is None:
            # title
            title = con.find('span', class_='list-article-item-title').text
            if new_title(title):
                # subTitle
                desc = con.find('h4').text
                link = con.find('a')['href']
                post = con.findAll('span')[1].text
                split_post = post.split(" ")
                date = split_post[len(split_post) - 2]
                time = split_post[len(split_post) - 1]
                print("Found new article in " + web + " category : " + cat)
                print(title)
                article_sport1(link, title, desc, web, cat, date, time)
                count += 1
    return count


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
        first_title = soup.find('div', class_="row category-article category-main-article")
        title = first_title.find('span', class_="category-top-story-title").text
        if new_title(title):
            desc = first_title.find('h4').text
            post = first_title.findAll('span')[1].text.split(" ")
            date = post[len(post) - 2]
            time = post[len(post) - 1]
            print("Found new article in " + web + " category : " + cat)
            print("Main : " + title)
            article_sport1(first_url, title, desc, web, cat, date, time)
            return 1
        else:
            return 0
    except:
        print("Error in first article")
        return 0


def get_all_titles_from_sport1(url_page, web="sport1", cat="israeli_football"):
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
    content = soup.find('div', id="PositionDivInPage2")
    count_new_article += main_title(content, soup, web, cat)
    count_new_article += second_titles(content, web, cat)
    return count_new_article


def article_sport1(url_page, title, desc, web, cat, date, time):
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
        context = soup.find('div', class_="article-inner-content").text
        insert_new_article(web, cat, title, desc, url_page, context, date, time)
    except:
        print("Error !  " + url_page)


def update_articles():
    """
    This method control update article of this web site
    :return: Number of new articles
    """
    count_new_article_all = 0
    print("Start.. update article in sport1")
    for league in all_league_sport1:
        count_new_article_all += get_all_titles_from_sport1(all_league_sport1[league], "sport1", league)
    print("Finish.. update article in sport1\n")
    return count_new_article_all
