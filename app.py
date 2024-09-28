from flask import Flask, render_template
from data_visualitation import generate_seaborn_plo

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/charts')
def charts():
    generate_seaborn_plo()
    return render_template("charts.html")

if __name__ == '__main__':
    app.run()
