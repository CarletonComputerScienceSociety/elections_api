# FLASK
from flask import Flask, request
app = Flask(__name__)

# ENV
from dotenv import load_dotenv

# TINYDB
from tinydb import TinyDB, Query

# Other
import os, urllib, subprocess, json

# Other functions
from util.functions import *

load_dotenv()

CCSS_SHARED_KEY = os.getenv("CCSS_SHARED_KEY")
CCSS_IV = os.getenv("CCSS_IV")

vote_database = TinyDB('database/database.json')
vote_query = Query()
candidates = load_candidates()

log_database = TinyDB('database/log.json')

# Only need to accept post requests, can ignore everything else
@app.route('/', methods=['POST'])
def vote():
    scs_key_url_encrypted = request.form['scs_key']
    client_vote = request.form['vote']

    log_database.insert({
        'key': scs_key_url_encrypted,
        'vote': client_vote
    })

    # The key is sent url encrypted by the SCS, so it needs to be decoded
    scs_encrypted_key = urllib.parse.unquote(scs_key_url_encrypted)

    # The decryption is done in a subprocess in PHP because
    # decryption is not working in Python
    scs_decryption_process = subprocess.run(
        ['php', 'util/decrypt.php', CCSS_SHARED_KEY, CCSS_IV],
        stdout=subprocess.PIPE,                     # The output from the PHP script
        input=bytes(scs_encrypted_key, 'utf-8'),    # Passed as input to prevent command line injection
        check=True
    )
    
    separated = str(scs_decryption_process.stdout).split(" ")
    time = separated[0].split("=")[1]
    user = separated[1].split("=")[1]
    ip = separated[2].split("=")[1]

    # If we get this far without an error, then we know that the user's
    # ciphertext is valid, and was encrypted by the SCS.

    duplicate_user_votes = vote_database.search(vote_query.user == user)

    print(len(duplicate_user_votes))

    result = validate_vote(client_vote, candidates)

    if (result[0] == 1):
        vote_database.insert({
            'time': time,
            'user': user,
            'ip': ip,
            'vote': client_vote
        })

        if (len(duplicate_user_votes) > 0):
            return "You have already voted! We deleted your old vote and replaced it with this one."
        else:
            return "Your vote was recorded! Thanks so much for voting in the CCSS general elections!"
    else:
        return result[1]

if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    app.run(
       debug=False,
       host="0.0.0.0",
    )