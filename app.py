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
# __            __         __
#|  |_.--.--.--|  |_.--.--|  |_
#|   _|  |  |  |   _|_   _|   _|
#|____|________|____|__.__|____|
#
# twtxt is an open, distributed
# microblogging platform that
# uses human-readable text files,
# common transport protocols, and
# free software.
#
# Learn more about twtxt at https://github.com/buckket/twtxt
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
        date, *content = line.split("\t")
        dt = parser.parse(date)
        formatted_date = str(dt.astimezone(pytz.timezone('Europe/London'))).replace(" ", "T")
        formatted_lines.append("\t".join([formatted_date, "".join(content)]))

    body = HEADER + "\n".join(formatted_lines)
    return Response(body, mimetype='text/plain')
