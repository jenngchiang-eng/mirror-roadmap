import os, http.server, socketserver
os.chdir('/tmp/mirror-roadmap')
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('127.0.0.1', 8765), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
