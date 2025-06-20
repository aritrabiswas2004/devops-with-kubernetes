from flask import Flask

app = Flask(__name__)

COUNT = -1

@app.route('/pingpong')
def hello():
    global COUNT
    COUNT += 1
    yield f"pong {COUNT}"

if __name__ == '__main__':
    app.run("0.0.0.0", port=4040)

