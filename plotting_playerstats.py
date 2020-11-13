#pip install mplcursors
from getplayerstats import scrapeplayerstats
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import mplcursors

point = []
reb = []
players = []
labels = []

def plot():
    year = input("year: ")
    file = 'data/playerdata/' + year + '.htm'
    with open(file, 'r', encoding='utf-8') as f:
            reading = f.read()
    soup = BeautifulSoup(reading, 'html.parser')
    content = soup.html.select("td", {'target' : '_blank'})

    for i in range(1, 50):
        players.append(content[(30 *(i-1)) + 1].text.strip('\n'))

    for name in players:
        stats = scrapeplayerstats(name, year)
        points = float(stats['pts'])
        rebounds = float(stats['oreb']) + float(stats['dreb'])
        point.append(points)
        reb.append(rebounds)
        labels.append(name)

    
    plt.plot(point, reb, 'ob')
    plt.xlim(xmin=min(point)-5, xmax=max(point) + 5)
    plt.ylim(ymin=min(reb)-0.5, ymax=max(reb)+0.5)       
    plt.ylabel("Rebounds")
    plt.xlabel("Points")
    mplcursors.cursor(hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(labels[sel.target.index]))
    plt.show()

 

plot()