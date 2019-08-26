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

def _format_timestamp(date):
    # TODO Make this configurable
    csv_tz = pytz.timezone('Europe/London')
    dt = parser.parse(date).replace(tzinfo=csv_tz)
    formatted_date = '{:%FT%T%z}'.format(dt.astimezone(pytz.UTC))
    return formatted_date


@app.route('/')
def twtxt():
    response = requests.get(GSHEET_URL)

    twtxts = response.text.replace(",", "\t")
    formatted_lines = []
    for line in twtxts.split("\n"):
        date, *content = line.split("\t")
        formatted_lines.append("\t".join([_format_timestamp(date), "".join(content)]))

    body = HEADER + "\n".join(formatted_lines)
    return Response(body, mimetype='text/plain')
