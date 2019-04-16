from urllib import response
from bs4 import BeautifulSoup
import requests
import json
import urllib
import re
import urllib.request


def split_titles(titles):
    dic = {}
    for title in titles:
        title_split = title.split(">")
        x=4


url = "https://www.sport5.co.il/world.aspx?FolderID=4439&lang=he"
regex = r'<h2><a href=(.+?)</a></h2>'
pattern = re.compile(regex)

with urllib.request.urlopen(url) as response:
   html = response.read().decode('utf-8')

title = re.findall(pattern, html)
split_titles(title)


# home_page = "https://www.sport5.co.il/"
# israeli_football = "https://www.sport5.co.il/world.aspx?FolderID=4439&lang=he"
# world_football = "https://www.sport5.co.il/world.aspx?FolderID=4453&lang=he"
# israeli_basketball = "https://www.sport5.co.il/world.aspx?FolderID=4467&lang=he"
# nba = "https://nba.sport5.co.il/NBA.aspx?FolderId=402&lang=HE"
#
# r = requests.get(israeli_football)
# dic = json.loads(r.text)
# print(dic)
#
