from flask import render_template
from flask_app import app
from flask_app.models import user

@app.route('/view_users')
def view_users():
    all_users = user.User.view_users()
    return render_template('/read_all.html',all_users = all_users)
