# -*- coding: utf-8 -*-
import BaseHTTPServer
from jinja2 import Template

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)                      
		self.send_header('Content-type','text/html')
		self.end_headers()                          
		template = Template('<html><body>Hello, {{name}} !</body></html>')
		self.wfile.write(template.render(name='John Doe'))
		return

print "Listening on port 8000..."
server = BaseHTTPServer.HTTPServer(('', 8000), MyHandler)
server.serve_forever()