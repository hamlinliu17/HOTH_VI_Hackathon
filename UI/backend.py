from flask import Flask, render_template, request
from data.linear_regression_model import*

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Webapp.html')

@app.route('/generate_results')
def function:
    return request.args.get("home_team")







if __name__ == '__main__':
    app.run(host = '0.0.0.0')
