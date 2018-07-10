#!/usr/bin/env python

"""
Very simple HTTP server in python.
Usage::
    ./web.py 
Send a GET request::
    curl http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

# Get port from environment variable or choose 9099 as local default
PORT = int(os.getenv("PORT", 9099))

class S(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.wfile.write("Hello. Test")
        
def run(server_class=HTTPServer, handler_class=S, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()