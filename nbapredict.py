from getstats import scrapestats

team = input('Team: ')
year = input('Year: ')
stats = scrapestats(team, year)

offensive = round(((stats['pts'] * stats['fgm'] * stats['fg%'] * stats['3pm'] *
            stats['3p%'] * stats['ftm'] * stats['ft%'] * stats['oreb'] * stats['ast']) * (
            100/42934758738941.51)), 2)

defensive = round((((stats['dreb'] *
            stats['stl'] * stats['blk'])/stats['tov']) * (100/142)), 2)

print(offensive)
print(defensive)
total = round((offensive + defensive + stats['win%']*10) * 100/214.7, 2)
print(total)
