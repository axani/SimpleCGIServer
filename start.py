#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
import webbrowser
import os
import socket, errno
 
# via: http://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/


def toggleServer():
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    try:
        server_address = ("", 8888)
        handler.cgi_directories = ["/cgi-bin"]
        httpd = server(server_address, handler)

        changeFilePermissions()
        openWebsite() 

        print 'Server started at http://0.0.0.0:8888/'
        httpd.serve_forever()

    except socket.error, v:
        server.shutdown
        print 'Server closed!'

def openWebsite():
    new = 2 # open in a new tab, if possible

    # open a public URL, in this case, the webbrowser docs
    url = "http://0.0.0.0:8888/index.html"
    webbrowser.open(url,new=new)

def changeFilePermissions():
    os.chmod('cgi-bin/test.cgi', 0755)

toggleServer()
# stopServer()