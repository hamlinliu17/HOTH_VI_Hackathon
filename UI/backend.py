from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Webapp.html')

@app.route('/generate_results')
def home_team():
    home_team = request.args.get('home_team')
    return home_team





if __name__ == '__main__':
    app.run(host = '0.0.0.0')
