#API_TOKEN = open("./apitoken.txt").read()
import sys
API_TOKEN = sys.argv[1]

DEFULT_REPLY = "not known word"

PLUGINS = [
    'slackbot.plugins' ,
    'botmodule' ,
    'botmodule2',
]