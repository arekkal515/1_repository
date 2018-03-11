# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:47:41 2018

@author: Arek
"""

# app.py
from flask import request


@app2.route('/request')
def request_info():
    return f'request method: {request.method} url: {request.url} headers: {request.headers}'