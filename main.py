# FLASK
from flask import Flask, request
app = Flask(__name__)

# ENV
from dotenv import load_dotenv
import os
load_dotenv()

# TINYDB
from tinydb import TinyDB, Query
db = TinyDB('database.json')

# URLLib
import urllib

# Other
import subprocess

CCSS_SHARED_KEY = os.getenv("CCSS_SHARED_KEY")
CCSS_IV = os.getenv("CCSS_IV")

# Only need to accept post requests, can ignore everything else
@app.route('/', methods=['POST'])
def vote():
    return "Working"
    scs_key_url_encrypted = request.form['scs_key']
    client_vote = request.form['vote']

    scs_encrypted_key = urllib.parse.unquote(scs_key_url_encrypted)
    scs_decryption_process = subprocess.run(
        ['php', 'decrypt.php', CCSS_SHARED_KEY, CCSS_IV],
        stdout=subprocess.PIPE,                     # The output from the PHP script
        input=bytes(scs_encrypted_key, 'utf-8'),    # Passed as input to prevent command line injection
        check=True
    )

    separated = str(decryption_process.stdout).split(" ")
    time = separated[0].split("=")[1]
    user = separated[1].split("=")[1]
    ip = separated[2].split("=")[1]

    # If we get this far without an error, then we know that the user's
    # ciphertext is valid, and was encrypted by the SCS.

    db.insert({
        'time': time,
        'user': user,
        'ip': ip,
        'vote': client_vote
    })

    return "{ok\:Your vote was recorded! Thanks so much for voting in the CCSS general elections!}"

if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    app.run(
       debug=False,
       host="0.0.0.0",
    )