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
        return "Arsenal wins"
    elif  value ==  1:
        return "Bournemoth wins"
    elif value == 3:
        return "Burnley wins"
    elif value == 5:
        return "Chelsea wins"
    elif value == 6:
        return "Crystal Palace wins"
    elif value == 7:
        return "Everton wins"
    elif value == 24:
        return "Hull City wins"
    elif value == 10:
        return "Leicester City wins"
    elif value == 11:
        return "Liverpool wins"
    elif value == 12:
        return "Manchester City wins"
    elif value == 13:
        return "Manchester United wins"
    elif value == 25:
        return "Middlesborough wins"
    elif value == 15:
        return "Southampton wins"
    elif value == 20:
        return "Stoke City wins"
    elif value == 26:
        return "Sunderland wins"
    elif value == 21:
        return "Swansea City wins"
    elif value == 16:
        return "Tottenham wins"
    elif value == 2:
        return "Watford wins"
    elif value == 23:
        return "West Bromwich wins"
    elif value == 18:
        return "West Ham United wins"
    elif value == 2:
        return "Brighton wins"
    elif value == 9:
        return "Huddersfeld wins"
    elif value == 50:
        return "draw"
    else:
        return value




if __name__ == '__main__':
    app.run(host = '0.0.0.0')
