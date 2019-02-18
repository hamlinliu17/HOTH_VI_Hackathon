from flask import Flask, render_template, request
from linear_regression_model import *


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Webapp.html')

@app.route('/generate_results')

def results():
    home_team = request.args.get('home_team')
    away_team = request.args.get('away_team')
    newValue = winner(home_team, away_team)
    value = int(newValue)
    if value == 0:
        return "Arsenal"
    elif  value ==  1:
        return "Bournemoth"
    elif value == 3:
        return "Burnley"
    elif value == 5:
        return "Chelsea"
    elif value == 6:
        return "Crystal Palace"
    elif value == 7:
        return "Everton"
    elif value == 24:
        return "Hull City"
    elif value == 10:
        return "Leicester City"
    elif value == 11:
        return "Liverpool"
    elif value == 12:
        return "Manchester City"
    elif value == 13:
        return "Manchester United"
    elif value == 25:
        return "Middlesborough"
    elif value == 15:
        return "Southampton"
    elif value == 20:
        return "Stoke City"
    elif value == 26:
        return "Sunderland"
    elif value == 21:
        return "Swansea City"
    elif value == 16:
        return "Tottenham"
    elif value == 2:
        return "Watford"
    elif value == 23:
        return "West Bromwich"
    elif value == 18:
        return "West Ham United"
    elif value == 2:
        return "Brighton"
    elif value == 9:
        return "Huddersfeld"
    elif value == 50:
        return "draw"
    else:
        return value




if __name__ == '__main__':
    app.run(host = '0.0.0.0')
