#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
From Book Django programming.

A simple cgi-server.

"""
from http.server import HTTPServer, CGIHTTPRequestHandler

httpd = HTTPServer(('127.0.0.1', 8080), CGIHTTPRequestHandler)
print("Web server starting...")
httpd.serve_forever()
