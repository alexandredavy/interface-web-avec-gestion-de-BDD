#	coding: utf-8
import http.server

port = 80
adress =("",port)

server = http.server.HTTPServer

Handler = http.server.CGIHTTPRequestHandler
Handler.cgi_directories = ["/"]

httpd = server(adress,Handler)

print(f"serveur démarrer sur le port :{port}")

httpd.serve_forever()