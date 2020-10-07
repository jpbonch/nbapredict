import requests
from lxml import html


def scrapestats(url):
    page = requests.get(url)
    root = html.fromstring(page.text)
    tree = root.getroottree()
    result = root.xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr[1]/td[6]')

    return result


    # stats = {'win': winpercentage}
    # return statsx
