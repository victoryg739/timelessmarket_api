from flask import Flask
from scrap import scrapData
app = Flask(__name__)

#Later change to production deployment

@app.route('/')
def hello_world():
    return "Nothing to see here"

@app.route("/fundamental/<query>")
def search_query(query):
    return scrapData(query)



if __name__ == '__main__':
    app.run()