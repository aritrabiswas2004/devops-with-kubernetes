from flask import Flask
import requests

app = Flask(__name__)

def read_pongs():
    # try:
    #     with open("/logs/pongs.log", "r") as fileptr:
    #         return fileptr.read()
    # except FileNotFoundError:
    #     return "No pingi-pongo yet!"
    try:
        response = requests.get("http://ping-pong-svc:3456/pings") # change this

        if response.status_code == 200:
            return response.content.decode() # f"{response.content}"
        else:
            return f"STATUS: {response.status_code} -- Something went wrong"
    except Exception as e:
        return f"ERROR -> {e}"

def read_contents():
    try:
        with open("/logs/outputs.log", "r") as fileptr:
            return fileptr.read()
    except FileNotFoundError:
        return "No logs yet"

@app.route('/')
def main():
    return f"{read_contents()}\n{read_pongs()}", {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run("0.0.0.0", port=3000)

