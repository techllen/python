from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models import user

# this route redirect users to the index/home page
@app.route('/')
def home():
    return render_template('index.html')
# this route handles user registration
@app.route('/register', methods = ['POST'])
def register():
    data = {
       'first_name': request.form['first_name'],
       'last_name': request.form['last_name'],
       'email': request.form['email'],
       'password': request.form['password']
    }
    user_id = user.User.register_user(data)
    return redirect('/')
    
# this route handles user login
@app.route('/login', methods = ['POST'])
def login():
    data = {
        'email': request.form['email'],
    }
    user_in_database = user.User.verify_user(data)
    # chacking if the password match
    if (request.form['password'] == user_in_database.password):
        # if user is in the database create a session for this user
        session['user_id'] = user_in_database.id
        # making path that includes user_name
        dashboard_path = '/dashboard/'+str(user_in_database.first_name)
        return redirect(dashboard_path)
    else:
        return redirect('/')
# this route directs the user to the dashboard page and display his name
@app.route('/dashboard/<string:user_name>')
def dashboard(user_name):
    return render_template('dashboard.html',first_name = user_name)