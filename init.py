"""
 This script is responsible for creating a flask web-server application
 to communicate to a client. The server has a method processText that returns
 the number of words in certain text.

 Author: Fernando Rodrigues Jr
 Date  : 28/02/2018

"""
# coding=utf-8
# Developed and tested with:
#
# os:             Ubuntu Xenial (16.04)
# python version: Python 3.5

# Notes:
# The code was created using a virtualenv, please run pip install -r requirements.txt
# To run the code: python init.py

from flask import Flask                 # Web-server
from flask import render_template       # render html template
from flask import request               # request handling
from flask import jsonify               # Json transformer
import spacy                            # lib to tokenize the text and extract words
from spacy.tokenizer import Tokenizer
nlp = spacy.load('en')                  # load english model (you should download it first)
tokenizer = Tokenizer(nlp.vocab)        # create tokenizer object using english model

# Start flask application
app = Flask(__name__)
app.debug = True # Show index content (main.html)
@app.route('/')
def showIndex():
    return render_template('main.html')

# Process received data and extract the number of words
# using spaCY library
@app.route('/processText', methods= ['POST'])
def processText():

    # request form data
    requestData = request.form

    # check if the request key is presented
    if 'bagOfText' not in requestData:
        response = jsonify(dict(wordCounter=0, errorMsg="Invalid Format"))
        response.status_code = 406
        return response

    # check if the input is not empty
    elif requestData['bagOfText'] == '':
        response = jsonify(dict(wordCounter=0, errorMsg="Input text is required!"))
        response.status_code = 200
        return response

    # count and return the number of words
    else:
        tokens = tokenizer(requestData['bagOfText'])
        response = jsonify(dict(wordCounter=len(tokens), errorMsg=""))
        response.status_code = 200
        return response

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)