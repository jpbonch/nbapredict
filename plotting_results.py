#plots two things on a graph
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from getstats import scrapestats

year = input("Year: ")
howmany = int(input("how many teams to plot: "))

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

    img = mpimg.imread('bulls.png', 0)


        
    points = stats['pts']
    rebounds = stats['dreb'] + stats['oreb']

    plt.plot(offensive, defensive, 'ro')
    plt.annotate(label, (offensive, defensive))




plt.xlabel('Offensive')
plt.ylabel('Defensive')    
plt.show()

