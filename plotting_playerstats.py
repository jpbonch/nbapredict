#pip install mplcursors
from getplayerstats import scrapeplayerstats
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import mplcursors

x_list = []
y_list = []
players = []
labels = []

def plot(x, y):
    year = input("year: ")
    file = 'data/playerdata/' + year + '.htm'
    with open(file, 'r', encoding='utf-8') as f:
            reading = f.read()
    soup = BeautifulSoup(reading, 'html.parser')
    content = soup.html.select("td", {'target' : '_blank'})

    for i in range(1, 20):
        players.append(content[(30 *(i-1)) + 1].text.strip('\n'))

    for name in players:
        stats = scrapeplayerstats(name, year)
        x_point = float(stats[x.lower()])
        y_point = float(stats[y.lower()])
        x_list.append(x_point)
        y_list.append(y_point)
        labels.append(name)

    
    plt.plot(x_list, y_list, 'ob')
    plt.xlim(xmin=min(x_list)-2, xmax=max(x_list) + 2)
    plt.ylim(ymin=min(y_list)-0.5, ymax=max(y_list)+0.5)       
    plt.ylabel(y)
    plt.xlabel(x)
    plt.title(f"{year} : {x} against {y}")
    mplcursors.cursor(hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(labels[sel.target.index] + f" {x}: {x_list[sel.target.index]} " + f"{y}: {y_list[sel.target.index]}"))

  
    plt.show()

 

plot("Points", "Rebounds")