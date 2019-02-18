from flask import Flask, render_template, request
from data import winner
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Webapp.html')

@app.route('/generate_results')
def results():
    home_team = request.args.get('home_team')
    away_team = request.args.get('away_team')
    result = winner(home_team, away_team)
    return result



if __name__ == '__main__':
    app.run(host = '0.0.0.0')
