from flask import Flask, render_template, request
from linear_regression_model import *


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Webapp.html')

@app.route('/generate_results')

#def goals():
    #home_team = request.args.get('home_team')
    #away_team = request.args.get('away_team')
    #goalsList = predict(home_team, away_team)
    #int(team1Goal) = goalsList[0]
    #int(team2Goal) = goalsList[1]
    #return str(int(team1Goal))

def results():
    home_team = request.args.get('home_team')
    away_team = request.args.get('away_team')
    newValue = winner(home_team, away_team)
    value = int(newValue)
    goalsList = predict(home_team, away_team)
    team1Goal = goalsList[0]
    team2Goal = goalsList[1]
    if(away_team == home_team):
        return "Invalid Input"
    if(team1Goal > team2Goal):
        if value == 0:
            return "Arsenal Wins  With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif  value ==  1:
            return "Bournemoth Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 3:
            return "Burnley Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 5:
            return "Chelsea Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 6:
            return "Crystal Palace Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 7:
            return "Everton Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 24:
            return "Hull City Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 10:
            return "Leicester City Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 11:
            return "Liverpool Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 12:
            return "Manchester City Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 13:
            return "Manchester United Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 25:
            return "Middlesborough Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 15:
            return "Southampton Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 20:
            return "Stoke City Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 26:
            return "Sunderland Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 21:
            return "Swansea City Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 16:
            return "Tottenham Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 2:
            return "Watford Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 23:
            return "West Bromwich Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 18:
            return "West Ham United Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 2:
            return "Brighton Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 9:
            return "Huddersfeld Wins With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        elif value == 50:
            return "Draw With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        else:
            return value
    elif(team1Goal < team2Goal):
        if value == 0:
            return "Arsenal Wins  With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif  value ==  1:
            return "Bournemoth Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 3:
            return "Burnley Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 5:
            return "Chelsea Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 6:
            return "Crystal Palace Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 7:
            return "Everton Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 24:
            return "Hull City Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 10:
            return "Leicester City Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 11:
            return "Liverpool Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 12:
            return "Manchester City Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 13:
            return "Manchester United Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 25:
            return "Middlesborough Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 15:
            return "Southampton Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 20:
            return "Stoke City Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 26:
            return "Sunderland Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 21:
            return "Swansea City Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 16:
            return "Tottenham Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 2:
            return "Watford Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 23:
            return "West Bromwich Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 18:
            return "West Ham United Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 2:
            return "Brighton Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 9:
            return "Huddersfeld Wins With Score " + str(int(team2Goal)) + " - " + str(int(team1Goal))
        elif value == 50:
            return "Draw With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))
        else:
            return value
    else:
        return "Draw With Score " + str(int(team1Goal)) + " - " + str(int(team2Goal))


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
