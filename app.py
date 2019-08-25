import os

from dateutil import parser
from flask import Flask, Response
import pytz
import requests


app = Flask(__name__)

GSHEET_URL = os.environ.get("GSHEET_URL")
TWTXT_USERNAME = os.environ.get("TWTXT_USERNAME")
TWTXT_URL = os.environ.get("TWTXT_URL")

HEADER = f"""
#
# twtxt is an open, distributed microblogging platform
#
# == Metadata ==
#
# nick = {TWTXT_USERNAME}
# url = {TWTXT_URL}
# user_agent = twtxt.xyz (+http://twtxt.xyz)
#
# == Content ==
#
"""

@app.route('/')
def twtxt():
    response = requests.get(GSHEET_URL)

    twtxts = response.text.replace(",", "\t")
    formatted_lines = []
    for line in twtxts.split("\n"):
        date, content = line.split("\t")
        dt = parser.parse(date)
        formatted_date = dt.astimezone(pytz.timezone('Europe/London'))
        formatted_lines.append("\t".join([str(formatted_date), content]))

    body = HEADER + "\n".join(formatted_lines)
    return Response(body, mimetype='text/plain')
