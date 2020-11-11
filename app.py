from flask import Flask, render_template, request
from getstats import scrapestats

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    teams = []
    teamstats = []
    return render_template('index.html', teamstats=teamstats, teams=teams)

@app.route("/form", methods=['GET', 'POST'])
def form():
    year = request.form.get('years')
    


if __name__ == "__main__":
    app.run()
