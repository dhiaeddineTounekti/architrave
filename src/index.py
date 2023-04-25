from flask import Flask
from utils import dbConnector

app = Flask(__name__)
# Connect to databases
dbConnector.connect()

@app.route('/')
def index():
    return 'Hello World!'