from flask import Flask

app = Flask(__name__)

COUNT = -1

def write_pongs_to_file(pongs):
    with open("/logs/pongs.log", "w") as fileptr:
        fileptr.write(f"Ping / Pongs: {pongs}\n")

@app.route('/pings')
def get_pings():
    return f"Ping / Pongs: {COUNT}" if COUNT > 0 else "Ping / Pongs: No pingi-pongo yet!"

@app.route('/pingpong')
def hello():
    global COUNT
    COUNT += 1
    # write_pongs_to_file(COUNT)
    yield f"pong {COUNT}"

if __name__ == '__main__':
    app.run("0.0.0.0", port=4040)

