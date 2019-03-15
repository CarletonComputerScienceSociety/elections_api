# CCSS Elections API

This is a server that will record votes from students for CCSS elections. 

The API recieves an AES-256 encrypted ciphertext from the SCS that verifes that it is in fact a student voting. Inside the decrypted ciphertext is a hashed version of the student number is used to identiy unique students. This prevents the CCSS from knowing how specific students voted. Also, no data is sent back to the SCS, so they do not have any information on how students voted either.

## File information

### .env
Environment variables for the server, it is gitignored so it is not seen on the repo.

### .gitignore
Prevents certain files from being checked into Git.

### database.json
Stores all of the votes. Not on the repo because it is generated on the server.

### decrypt.php
Used to decrypt the AES-256 ciphertext from the SCS.

### docker-compose.yml
Used to run the server, as well as a reverse proxy with SSL.

### Dockerfile
Dictates how to build an image that will run the Python server.

### generate_env.py
Generates a .env file for the SCS secret keys.

### Licence
Standard MIT licence.

### server.py
The Flask server that listens for votes.