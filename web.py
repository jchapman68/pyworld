#!/usr/bin/env python

"""
Very simple HTTP server in python.
Usage::
    ./web.py 
Send a GET request::
    curl http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.wfile.write("Hello. Test")
        
def run(server_class=HTTPServer, handler_class=S, port=8090):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()