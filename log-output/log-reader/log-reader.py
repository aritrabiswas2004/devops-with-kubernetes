from flask import Flask

app = Flask(__name__)

def read_pongs():
    try:
        with open("/logs/pongs.log", "r") as fileptr:
            return fileptr.read()
    except FileNotFoundError:
        return "No pingi-pongo yet!"

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

