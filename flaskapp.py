from flask import Flask
from parser import parse_date

app = Flask(__name__)


@app.route("/")
def hello_world():
    raw_date = "tomorrow at noon"
    return parse_date(raw_date)

if __name__ == "__main__":
    app.run()
