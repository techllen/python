from flask import Flask
# importing secret module to randomly generating hexadecimal secret keys for the sessions
import secrets
app = Flask(__name__)
app.secret_key= secrets.token_hex()
