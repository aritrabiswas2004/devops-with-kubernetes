from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="postgres-svc",
    port=5432,
    dbname="pongsdb",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

def init_db():
    cur.execute("CREATE TABLE IF NOT EXISTS pongs (pong_count int)")

    cur.execute("SELECT COUNT(*) FROM pongs")
    count = cur.fetchone()[0]

    if count == 0:
        cur.execute("INSERT INTO pongs (pong_count) VALUES (0)")

    conn.commit()

init_db()

def write_pongs_to_db():
    try:
        cur.execute("UPDATE pongs SET pong_count = pong_count + 1")
    except Exception as e:
        print("Exception Occurred -> ", e)

def read_pongs_from_db():
    cur.execute("SELECT * FROM pongs")
    value = cur.fetchall()[0][0]

    return value

@app.route('/pings')
def get_pings():
    count = read_pongs_from_db()
    return f"Ping / Pongs: {count}" if count > 0 else "Ping / Pongs: No pingi-pongo yet!"

@app.route('/pingpong')
def hello():
    write_pongs_to_db()
    return f"pong {read_pongs_from_db()}", {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run("0.0.0.0", port=4040)

# from flask import Flask
#
# app = Flask(__name__)
#
# COUNT = -1
#
# def write_pongs_to_file(pongs):
#     with open("/logs/pongs.log", "w") as fileptr:
#         fileptr.write(f"Ping / Pongs: {pongs}\n")
#
# @app.route('/pings')
# def get_pings():
#     return f"Ping / Pongs: {COUNT}" if COUNT > 0 else "Ping / Pongs: No pingi-pongo yet!"
#
# @app.route('/pingpong')
# def hello():
#     global COUNT
#     COUNT += 1
#     # write_pongs_to_file(COUNT)
#     return f"pong {COUNT}", {'Content-Type': 'text/plain'}
#
# if __name__ == '__main__':
#     app.run("0.0.0.0", port=4040)
#

