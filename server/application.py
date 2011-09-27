from flask import Flask, request, jsonify
from configuration import *
import math
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/getsentiment', methods=['POST'])
def sentiment_analysis():
    if 'text' not in request.form:
        return jsonify(ERROR_NOTEXT)
    
    file = open(AFINN_FILE, 'r')
    sentiment_dict = dict(map(lambda (w, s): (w, int(s)), [ws.strip().split('\t') for ws in file]))
    file.close()
    pattern_split = re.compile(r"\W+")
    words = pattern_split.split(request.form['text'].lower())
    sentiments = map(lambda word: sentiment_dict.get(word, 0), words)
    if sentiments:
        # How should you weight the individual word sentiments?
        # You could do N, sqrt(N) or 1 for example. Here I use sqrt(N)
        sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
    else:
        sentiment = 0
    return jsonify(status='success', sentiment=sentiment)