from flask import Flask
from scrap import scrapData
from yahoofin import scrap_yahoofin
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#Later change to production deployment

@app.route('/')
def hello_world():
    return "Nothing to see here"

@app.route("/fundamental/<query>")
def search_query(query):
    return scrapData(query)

@app.route("/yahoofin/<query>")
def search_yahoof(query):
    return scrap_yahoofin(query)


if __name__ == '__main__':
    app.run()
