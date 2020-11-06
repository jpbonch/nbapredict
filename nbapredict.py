# 2016 warriors: ((((1*114.8*42.7*49.5*11.9*38.3*17.6*78.8*44*30.1*9.5*6.7)/10)/20 + 11.5 * 10000000)/10**13)*(10/6.46469350606)
from getstats import scrapestats

team = input('Team: ')
year = input('Year: ')
stats = scrapestats(team, year)

offensive = round((((stats['win%'] * stats['pts'] * stats['fgm'] * stats['fg%'] * stats['3pm'] *
            stats['3p%'] * stats['ftm'] * stats['ft%'] * stats['reb'] * stats['ast'] *
            stats['stl'] * stats['blk'])/stats['tov']) / 10**13) * (100/60.91), 2)

print(offensive)
