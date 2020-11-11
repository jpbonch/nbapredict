#plots two things on a graph
#pip install opencv-python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
from getstats import scrapestats
from PIL import Image

year = input("Year: ")
howmany = int(input("how many teams to plot: "))


def getImage(path, zoom):
    return OffsetImage(plt.imread(path, 0), zoom=zoom)

offense = []
defense = []
paths = []

def graphing():

    for i in range(howmany):

        team = input("Team: ")
        stats = scrapestats(team, year)

        offensive = round(((stats['pts'] * stats['fgm'] * stats['fg%'] * stats['3pm'] *
                stats['3p%'] * stats['ftm'] * stats['ft%'] * stats['oreb'] * stats['ast']) * (
                100/42934758738941.51)), 2)

        defensive = round((((stats['dreb'] *
                stats['stl'] * stats['blk'])/stats['tov']) * (100/142)), 2)

        

        name = team.split(' ')
        if len(name) == 2:
            label = name[1]
        else:
            label = name[2]

    
        paths.append(f'Images/{label}.png')
        offense.append(offensive)
        defense.append(defensive)

        



    fig, ax = plt.subplots()
    ax.scatter(offense, defense) 

    for x0, y0, path in zip(offense, defense, paths):
        ab = AnnotationBbox(getImage(path, zoom=0.3), (x0, y0), frameon=False)
        ax.add_artist(ab)
        
    plt.xlim(xmin=min(offense)-10, xmax=max(offense)+10)
    plt.ylim(ymin=min(defense)-10, ymax=max(defense)+10)
    plt.xlabel('Offensive')
    plt.ylabel('Defensive')
    plt.show()

graphing()