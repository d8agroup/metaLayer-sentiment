from flask import Flask, request, jsonify
from configuration import *

app = Flask(__name__)

@app.route('/test')
def test():
    return "worked 2"
