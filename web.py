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
PORT = int(os.getenv("PORT", 9099))

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'