import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

SERVERPORT = int(os.environ.get('PORT', 8080))

def main():
    httpd = HTTPServer(('', SERVERPORT), SimpleHTTPRequestHandler)

    print(f"Started server in port {SERVERPORT}", flush=True)

    httpd.serve_forever()

if __name__ == '__main__':
    main()


