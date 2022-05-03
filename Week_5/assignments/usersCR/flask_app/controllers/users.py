from flask import render_template, request,redirect
from flask_app import app
from flask_app.models import user

# this route handles users to the view 
@app.route('/view_users')
def view_users():
    all_users = user.User.view_users()
    return render_template('/read_all.html',all_users = all_users)
# this route handles links add user button to create page
@app.route('/create_user_form')
def create_user_form():
    return render_template('/create.html')

#this route creates users 
@app.route('/create_user',methods=['POST'])
def create_user():
    # receiving data from the form and link them to the dictionary
    data = {
        'first_name':request.form['firstname'],
        'last_name':request.form['lastname'],
        'email':request.form['email']
    }
    # linking data to the dictionary object
    user.User.create_user(data)
    print(data)
    return redirect('/view_users')
# this route handles all the errors for resources not found
@app.errorhandler(404)
def errors(e):
    return render_template('error.html')