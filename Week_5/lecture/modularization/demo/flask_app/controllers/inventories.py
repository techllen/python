from flask import render_template,session,request,redirect
# import models as necessary
# import app from init file
from flask_app import app
@app.route('/')
def home():
    # validations
    # int with database
    # return template/redirect
    return render_template('all_inventories.html')

@app.route('/inventories')
def all_inventories():
    # validations
    # int with database
    # return template/redirect
    return render_template('all_inventories.html')