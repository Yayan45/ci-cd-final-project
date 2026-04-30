from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SERVICERUNNING")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Listening on port 8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()