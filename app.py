from flask import Flask
import requests


app = Flask(__name__)

HEADER = """
#
# twtxt is an open, distributed microblogging platform
#
# == Metadata ==
#
# nick = gil
# url = https://twtxt.herokuapp.com/
# user_agent = twtxt.xyz (+http://twtxt.xyz)
#
# == Content ==
#
"""

@app.route('/')
def twtxt():
    response = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vT5pcDrp03CkitXKjeTZ8PCwSXHbmEmtvQVidB6XdbjhgmIc8Y6snNZK5XZU2-VhapSXWPZwsSYNf6q/pub?output=csv")

    body = HEADER + response.text.replace(",", "\t")
    return body
