from dateutil import parser
from flask import Flask, Response
import pytz
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

    txtxts = response.text.replace(",", "\t")
    formatted_lines = []
    for line in twtxts:
        date, content = line.split("\t")[0], line.split(',')[:1]
        dt = parser.parse(date)
        date = dt.astimezone(pytz.timezone('Europe/London'))
        formatted_lines.append("\t".join([date, content]))

    body = HEADER + "\n".join(formatted_lines)
    return Response(body, mimetype='text/plain')
