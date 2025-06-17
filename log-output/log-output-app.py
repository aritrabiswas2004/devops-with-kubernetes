import time
from datetime import datetime as dt
import random

def gen_random_string(length):
    rnd_string = ""
    
    for i in range(length):
        rnd_string += random.choice([chr(random.randint(65, 90)), chr(random.randint(97, 122))])

    return rnd_string

while True:
    try:
        print(f"{dt.now()}: {gen_random_string(3)}-{gen_random_string(5)}-{gen_random_string(2)}", flush=True)
        time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...", flush=True)
        break

