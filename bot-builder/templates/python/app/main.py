from flask import Flask
from threading import Thread
from .bot import client

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello orld"

def run_bot():
    if client:
        client.run("<TOKEN HERE>")
    else:
        return 0

thread = Thread(target=run_bot)
thread.start()