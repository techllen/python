from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models import user,message
from flask_bcrypt import Bcrypt        
from datetime import datetime
bcrypt = Bcrypt(app)

# this route redirect users to the index/home page
@app.route('/')
def home():
    return render_template('index.html')
# this route handles user registration
@app.route('/register', methods = ['POST'])
def register():
    # first thing first validate your inputs
    if not user.User.user_validation(request.form):
        # if any user input is invalid send the user to home page
        return redirect('/')
    # hashing passwords using 15 rounds of salt
    password_hash = bcrypt.generate_password_hash(request.form['password'],15)
    # print(password_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        #assigning the password hash into the password dictionary key    
        'password': password_hash
    }
    # saving the data and assigning session to the user
    session['user_id'] = user.User.register_user(data)
    # session['first_name'] = request.form['first_name'] #used to display username in the wall page
    return redirect('/wall')

    
# this route handles user login
@app.route('/login', methods = ['POST'])
def login():
    data = {
        'email': request.form['email'],
    }
    found_user = user.User.verify_user(data)
    # chacking if the password match
    if not found_user:
        # flash error message
        user.User.user_login_validation('email_not_found')
        return redirect('/')
    if not bcrypt.check_password_hash(found_user.password,request.form['password']):
        # flash error message
        user.User.user_login_validation('password_not_correct')
        return redirect('/')
    #assigning session to the user
    session['user_id'] = found_user.id
    # session['first_name'] = found_user.first_name #used to display username in the wall page
    return redirect('/wall')

# this route directs the user to the wall page and display his name
@app.route('/wall')
def wall():
    """
    If the user attempts to access the success page (i.e. making a GET request by typing in the url), 
    redirect them back to the login and registration page.
    """
    # checking if the user is in session
    if session.get('user_id')==None:
        return redirect('/')
    else:
        data = {
            'id':session["user_id"]
        }
        this_user = user.User.get_one_user_by_id(data)
        users_to_display_on_the_wall = user.User.get_all_users()
        # getting all messages sent to me
        my_messages_list_result = message.Message.get_my_messages(data)
        # getting all messages user has sent to other people
        my_sent_messages_list_result = message.Message.get_all_sent_messages(data)
        # in case no messages for the user
        if len(my_messages_list_result) == 0 and len(my_sent_messages_list_result) == 0 :
            return render_template('wall.html',this_user = this_user,users = users_to_display_on_the_wall)
        else:
            return render_template('wall.html',this_user = this_user,users = users_to_display_on_the_wall,messages_sent_to_me = my_messages_list_result,today_date = datetime.now(),number_of_messages_sent = len(my_sent_messages_list_result))

# this route clears the sessions
@app.route('/logout')
def logout():
    session.clear()
    # print(str(session.get('user_id')))
    return redirect('/')
# this route redirects the user to the error page if the links is not found
@app.errorhandler(404)
def errors(e):
    return render_template('errorpage.html')
