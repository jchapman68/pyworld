#!/usr/bin/env python

"""
Very simple HTTP server in python.
Usage::
    ./web.py 
Send a GET request::
    curl http://localhost
"""
import os

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT"))

from flask import Flask
app = Flask(__name__)

import helloworld as hw

@app.route('/greeting/<name>')
def hello_world(name):
    return hw.test_greeting(name)

@app.route('/')
def health_check():
    return 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)