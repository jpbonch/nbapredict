from getstats import scrapestats
from getplayerstats import scrapeplayerstats

team = input('Team: ')
year = input('Year: ')
name = input('Name: ')
stats = scrapestats(team, year)
player_stats = scrapeplayerstats(name, year)

offensive = round(((stats['pts'] * stats['fgm'] * stats['fg%'] * stats['3pm'] *
            stats['3p%'] * stats['ftm'] * stats['ft%'] * stats['oreb'] * stats['ast']) * (
            100/42934758738941.51)), 2)

defensive = round((((stats['dreb'] *
            stats['stl'] * stats['blk'])/stats['tov']) * (100/151.28)), 2)

print('Offensive rating:', offensive)
print('Defensive rating:', defensive)
total = 'Total: ' + str(round((offensive + defensive + stats['win%']*10) * 100/208.17, 2))
print(total)
