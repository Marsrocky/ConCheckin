#!/usr/bin/env python
"""
Very simple HTTP server in python.

Usage::
    ./dummy-web-server.py [<port>]

Send a GET request::
    curl http://localhost

Send a HEAD request::
    curl -I http://localhost

Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost

"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import urllib, urllib2
import json

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("Register Success!")

        # Package analysis
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len).split('&')
        name = urllib.unquote(post_body[0]).split('=')[1]
        email = urllib.unquote(post_body[1]).split('=')[1]
        mac = urllib.unquote(post_body[2]).split('=')[1].upper()
        
        name = name.replace('+', ' ')
        # write json file to record
        newdic = {
            'name' : name,
            'email' : email,
            'mac' : mac
        }
        file = open('record.txt', 'r')
        text = file.read()
        tjson = json.loads(text)
        tjson.append(newdic)
        file.close()
        file = open('record.txt', 'w+')
        file.write(json.dumps(tjson))
        print 'Successful Recorded: ', name, ' ', email, ' ', mac

        
def run(server_class=HTTPServer, handler_class=S, port=2222):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting HTTP Registration Server...'
    httpd.serve_forever()

def init():
    init_data = [{'mac': '00:00:00:00:00:01', 'name': 'test', 'email': 'test'}]
    file = open('record.txt', 'w+')
    file.write(json.dumps(init_data))

if __name__ == "__main__":
    from sys import argv
    init()
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()