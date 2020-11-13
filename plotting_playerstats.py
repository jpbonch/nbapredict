from getplayerstats import scrapeplayerstats
import matplotlib.pyplot as plt

point = []
reb = []

players = ["Joel Embiid", "James Harden", "Anthony Davis", "LeBron James", "Kawhi Leonard"]

def plot(howmany):
    year = input("year: ")
    for name in players:
        stats = scrapeplayerstats(name, year)
        points = float(stats['pts'])
        rebounds = float(stats['oreb']) + float(stats['dreb'])
        point.append(points)
        reb.append(rebounds)
        plt.annotate(name, (points,rebounds))
    
    plt.plot(point, reb, 'ob')
    plt.xlim(xmin=min(point)-10, xmax=max(point) + 5)
    plt.ylim(ymin=min(reb)-10, ymax=max(reb)+10)       
    plt.ylabel("Rebounds")
    plt.xlabel("Points")
    plt.show()

plot(5)


    