from flask import Flask, render_template, request
from getstats import scrapestats
from getplayerstats import scrapeplayerstats


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    teams = []
    teamstats = []
    return render_template('index.html', teamstats=teamstats, teams=teams)

@app.route("/teamdata", methods=['GET', 'POST'])
def form():
    year = request.args.get('year')
    team = request.args.get('team')
    stats = scrapestats(team, year)

    offensive = round(((stats['pts'] * stats['fgm'] * stats['fg%'] * stats['3pm'] *
                stats['3p%'] * stats['ftm'] * stats['ft%'] * stats['oreb'] * stats['ast']) * (
                100/42934758738941.51)), 2)

    defensive = round((((stats['dreb'] *
                stats['stl'] * stats['blk'])/stats['tov']) * (100/151.28)), 2)

    total = round((offensive + defensive + stats['win%']*10) * 100/208.17, 2)

    return render_template('index.html', offensive=offensive, defensive=defensive, total=total)

@app.route('/playerdata')
def playerdata():
    name = request.args.get('name')
    playeryear = request.args.get('playeryear')
    print(name)
    print(playeryear)
    playerstats = scrapeplayerstats(name, playeryear)
    print(playerstats)
    return render_template('index.html', playerstats=playerstats)


if __name__ == "__main__":
    app.run()
