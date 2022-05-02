from flask import Flask
import secrets
app = Flask(__name__) #create app instance
# create session secret key
app.secret_key = secrets.token_hex()