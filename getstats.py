import requests
from bs4 import BeautifulSoup

teamranges = {
    'Milwaukee Bucks': 27

}



def scrapestats(url, team):

    teamrange = teamranges[team]

    with open('NBA.com_Stats _ Teams Traditional.html', 'r', encoding='utf-8') as f:
        reading = f.read()

    soup = BeautifulSoup(reading, 'html.parser')
    
    content = soup.html.select('td', {'target':'_blank'})

    stats=[]
    for i in range(840):
            stats.append(content[i].text.strip('\n').strip(' '))

    stats = [[stats[i]] for i in len(stats)]
    print(stats)




print(scrapestats('dumb', 'Milwaukee Bucks'))


    
