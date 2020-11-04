# 2016 warriors: ((((1*114.8*42.7*49.5*11.9*38.3*17.6*78.8*44*30.1*9.5*6.7)/10)/20 + 11.5 * 10000000)/10**13)*(10/6.46469350606)
year = input('Year: ')
from getstats import scrapestats
url = 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&SeasonType=Regular%20Season&Season=' + year + '&PerMode=Per100Possessions'
team = 'Milwaukee Bucks'
stats = scrapestats(url, team)

offensive = round(((stats['win%'] * stats['pts'] * stats['fgm'] * stats['fg%'] * stats['3pm'] *
            stats['3p%'] * stats['ftm'] * stats['ft%'] * stats['reb'] * stats['ast'] *
            stats['stl'] * stats['blk'])/stats['tov']) / 10**13, 2) * (100/60.91)

print(offensive)
