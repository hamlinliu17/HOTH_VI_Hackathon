from flask import Flask, render_template, request
from data.linear_regression_model import*
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Webapp.html')

@app.route('/generate_results')
def home_team():
    home_team = request.args.get('home_team')
    return home_team
def visit_team():
    away_team = request.args.get('away_team')
    return away_team

def results():
    result = winnter(home_team(), visit_team())
    return result



if __name__ == '__main__':
    app.run(host = '0.0.0.0')
