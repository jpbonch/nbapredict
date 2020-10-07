year = input('Year: ')
from getstats import scrapestats
url = 'https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&SeasonType=Regular%20Season&Season=' + year + '&PerMode=Per100Possessions'

staty = scrapestats(url)

print(staty)