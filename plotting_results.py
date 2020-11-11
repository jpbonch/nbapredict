import pandas as pd
import matplotlib.pyplot as plt
from getstats import scrapestats

year = input("Year: ")

for i in range(1):

    team = input("Team: ")
    stats = scrapestats(team, year)

    name = team.split(' ')
    if len(name) == 2:
        label = name[1]
    else:
        label = name[2]
        
    points = stats['pts']
    rebounds = stats['dreb'] + stats['oreb']

    plt.plot(points, rebounds, 'ro')
    plt.annotate(label, (points, rebounds))
    plt.xlabel('Points')
    plt.ylabel('Rebounds')
    plt.ylim(ymin=0)
    plt.xlim(xmin=90)
plt.show()

