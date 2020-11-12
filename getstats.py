import requests
from bs4 import BeautifulSoup


def scrapestats(team, year):
    file = 'data/teamdata/' + year + '.htm'
    with open(file, 'r', encoding='utf-8') as f:
        reading = f.read()

    soup = BeautifulSoup(reading, 'html.parser')

    content = soup.html.select('td', {'target':'_blank'})

    stats=[]
    rawstats=[]
    for i in range(840):
            rawstats.append(content[i].text.strip('\n').strip(' '))

    if int(year) >= 1997 and int(year) <= 2004:
        rawstats = rawstats[:-28]
    teamlist = [x for x in rawstats if x[0].isalpha()]

    for i in range(len(teamlist)):
        stats.append([None]*28)

    for teamy in range(len(teamlist)):
        for value in range(28):
            stats[teamy][value] = rawstats[0]
            rawstats.pop(0)

    for i in range(len(stats)):
        if stats[i][1] == team:
            row = stats[i]

    row = [float(x) if row.index(x) != 1 else x for x in row]

    statsdict = {}
    statnames = ['seed', 'team', 'gp', 'w', 'l', 'win%', 'min', 'pts', 'fgm', 'fga',
                'fg%', '3pm', '3pa', '3p%', 'ftm', 'fta', 'ft%', 'oreb', 'dreb',
                'reb', 'ast', 'tov', 'stl', 'blk', 'blka', 'pf', 'pfd', '+/-']
    for i in range(len(row)):
        statsdict[statnames[i]] = row[i]

    return statsdict
