import requests
from bs4 import BeautifulSoup

def scrapeplayerstats(name, year):
    file = 'data/playerdata/' + year + '.htm'
    with open(file, 'r', encoding='utf-8') as f:
            reading = f.read()

    soup = BeautifulSoup(reading, 'html.parser')

    content = soup.html.select("td", {'target' : '_blank'})


    lst = []

    for i in range(1, 50):
        for j in range(0, 30):
            if content[(30 *(i-1)) + 1].text.strip('\n') == name:
                lst.append(content[(30 *(i-1)) + j].text.strip('\n').strip(' '))


    stats = ['rank', 'name', 'team', 'age', 'gp', 'w', 'l','min', 'points', 'fgm', 'fga',
                    'fg%', '3pm', '3pa', '3p%', 'ftm', 'fta', 'ft%', 'oreb', 'dreb',
                    'rebounds', 'assists', 'turnovers', 'steals', 'blocks', 'pf', 'fp', 'dd2', 'td3', '+/-']

    statsdict = {}

    for i in range(len(lst)):
        statsdict[stats[i]] = lst[i]


    return statsdict
