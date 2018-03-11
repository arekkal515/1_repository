# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:35:16 2018

@author: Arek
"""

# app.py
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello!'


if __name__ == '__main__':
    app.run(debug=True)