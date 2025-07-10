import os
import requests
import time
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

start = time.time()
first_req = True
dirname = os.path.dirname(__file__)

@app.route('/todos', methods=['POST'])
def handle_todos():
    response = requests.post("http://todo-list-svc:4040/todos", data=request.form)
    if response.status_code == 200:
        return redirect("/")
    else:
        return "Something went wrong"

@app.route('/')
def main():
    global start
    global first_req

    last_refreshed = time.time()
    elapsed = abs(start - last_refreshed)

    if elapsed > 600 or first_req:
        first_req = False
        response = requests.get("https://picsum.photos/1200")

        if response.status_code == 200:
            # change when deploying in k8s
            with open(os.path.join(dirname, "static/image.jpg"), "wb") as fileptr:
                fileptr.write(response.content)

        start = last_refreshed

    response_todos = requests.get("http://todo-list-svc:4040/todos").json()

    return render_template("index.html", todos=response_todos)

if __name__ == '__main__':
    app.run("0.0.0.0", port=os.environ.get("PORT", 8080))

# import os
# from http.server import SimpleHTTPRequestHandler, HTTPServer
#
# SERVERPORT = int(os.environ.get('PORT', 8080))
#
# def main():
#     httpd = HTTPServer(('', SERVERPORT), SimpleHTTPRequestHandler)
#
#     print(f"Started server in port {SERVERPORT}", flush=True)
#
#     httpd.serve_forever()
#
# if __name__ == '__main__':
#     main()

