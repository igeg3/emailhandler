# import http.server
# import socketserver

# class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             self.path = 'index.html'
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)

# PORT = 8000

# def run_server():
#     handler = MyHttpRequestHandler
#     with socketserver.TCPServer(("", PORT), handler) as httpd:
#         print("Server started at localhost:" + str(PORT))
#         httpd.serve_forever()

# if __name__ == "__main__":
#     run_server()


import http.server
import socketserver
import os
import urllib.parse

PORT = 8000
WEB_ROOT = os.path.abspath(os.path.dirname(__file__))

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/generate-email'):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            # Parse query parameters
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)

            if 'companyName' in params and 'textBefore' in params and 'domain' in params:
                company_name = params['companyName'][0]
                text_before = params['textBefore'][0]
                domain = params['domain'][0]

                # Generate email address
                email = text_before + "@" + company_name + "." + domain

                # Send the generated email address as response
                self.wfile.write(email.encode())
            else:
                self.wfile.write(b'Error: Missing parameters')
        else:
            # Serve files from current directory
            try:
                # Attempt to serve the requested file
                return http.server.SimpleHTTPRequestHandler.do_GET(self)
            except FileNotFoundError:
                # If the requested file is not found, serve the index.html page
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open(os.path.join(WEB_ROOT, 'index.html'), 'rb') as file:
                    self.wfile.write(file.read())

def run_server():
    with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()

if __name__ == "__main__":
    os.chdir(WEB_ROOT)  # Change working directory to web root
    run_server()
