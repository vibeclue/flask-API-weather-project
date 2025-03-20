from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/api/v1/<station>/<date>')
def get_weather(station, date):
    return {"station": station,
            "date": date,
            "temperature": 12}


if __name__ == '__main__':
    app.run()
