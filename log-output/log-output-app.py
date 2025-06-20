# import time
# from datetime import datetime as dt
# import random
#
# def gen_random_string(length):
#     rnd_string = ""
#
#     for i in range(length):
#         rnd_string += random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])
#
#     return rnd_string
#
# while True:
#     try:
#         print(f"{dt.now()}: {gen_random_string(3)}-{gen_random_string(5)}-{gen_random_string(2)}", flush=True)
#         time.sleep(5)
#     except KeyboardInterrupt:
#         print("Exiting...", flush=True)
#         break

import time
from datetime import datetime as dt
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

latest_random_string = ""

def gen_random_string(length):
    rnd_string = ""
    for _ in range(length):
        rnd_string += random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])
    return rnd_string

def update_random_string():
    """Generates and updates the global random string every 5 seconds."""
    global latest_random_string
    while True:
        current_string = f"{gen_random_string(3)}-{gen_random_string(5)}-{gen_random_string(2)}"
        latest_random_string = current_string
        print(f"{dt.now()}: {latest_random_string}", flush=True)
        time.sleep(5)

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests for the root path."""
        if self.path == '/':
            self.send_response(200)
            # Change Content-type to text/plain
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(latest_random_string.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

def run_server():
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting server in {server_address[1]}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Exiting...", flush=True)
        httpd.server_close()

if __name__ == '__main__':
    string_updater_thread = threading.Thread(target=update_random_string, daemon=True)
    string_updater_thread.start()

    run_server()

