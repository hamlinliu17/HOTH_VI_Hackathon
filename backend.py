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
        return "Arsenal Wins!"
    elif  value ==  1:
        return "Bournemoth Wins!"
    elif value == 3:
        return "Burnley Wins!"
    elif value == 5:
        return "Chelsea Wins!"
    elif value == 6:
        return "Crystal Palace Wins!"
    elif value == 7:
        return "Everton Wins!"
    elif value == 24:
        return "Hull City Wins!"
    elif value == 10:
        return "Leicester City Wins!"
    elif value == 11:
        return "Liverpool Wins!"
    elif value == 12:
        return "Manchester City Wins!"
    elif value == 13:
        return "Manchester United Wins!"
    elif value == 25:
        return "Middlesborough Wins!"
    elif value == 15:
        return "Southampton Wins!"
    elif value == 20:
        return "Stoke City Wins!"
    elif value == 26:
        return "Sunderland Wins!"
    elif value == 21:
        return "Swansea City Wins!"
    elif value == 16:
        return "Tottenham Wins!"
    elif value == 2:
        return "Watford Wins!"
    elif value == 23:
        return "West Bromwich Wins!"
    elif value == 18:
        return "West Ham United Wins!"
    elif value == 2:
        return "Brighton Wins!"
    elif value == 9:
        return "Huddersfeld Wins!"
    elif value == 50:
        return "Draw!"
    else:
        return value




if __name__ == '__main__':
    app.run(host = '0.0.0.0')
