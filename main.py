import os
import pymongo
import sys
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
import requests

# x = requests.get('https://w3schools.com/python/demopage.htm')



def format_json_response(data):
    json_str = json.dumps(data, indent=4,sort_keys=True, default=str)
    print(highlight(json_str, JsonLexer(), TerminalFormatter()))

CHANGE_STREAM_DB="mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
client = pymongo.MongoClient(CHANGE_STREAM_DB)
change_stream = client.changestream.collection1.watch([{
    '$match': {
        'operationType': { '$in': ['insert','update'] }
    }
}])
for change in change_stream:
    format_json_response(change)

