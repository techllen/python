from flask import render_template, request,redirect
from flask_app import app
from flask_app.models import user

# index route redirect to read all page
@app.route('/')
def home():
    return redirect('/users')
# this route handles users to the view 
@app.route('/users')
def view_users():
    all_users = user.User.view_users()
    return render_template('/read_all.html',all_users = all_users)
# this route handles links add user button to create page
@app.route('/users/new')
def create_user_form():
    return render_template('/create.html')
#this route creates users 
@app.route('/form_handler',methods=['POST'])
def create_user():
    # receiving data from the form and link them to the dictionary
    data = {
        'first_name':request.form['firstname'],
        'last_name':request.form['lastname'],
        'email':request.form['email']
    }
    new_user_id = str(user.User.create_user(data))
    # print(data)
    # creating a string path for redirection to read one page
    show_user_page_path = '/users/'+ new_user_id
    return redirect(show_user_page_path)
# this route handles showing the details of a single user
@app.route('/users/<int:id>')
def view_user(id):
    data = {
        'id': id
    }
    user_to_view = user.User.show_one_user(data)
    # print(user_to_view)
    return render_template('/read_one.html',id= id,user_to_view = user_to_view)
# this route handles editing the details of a single user
@app.route('/users/<int:id>/edit')
def edit_user(id):
    # selecting the user from database and prepopulate the data in the HTML place holders
    data = {
        'id': id
    }
    user_info_to_populate = user.User.show_one_user(data)
    print(user_info_to_populate)
    return render_template('/edit_user.html',id = id,user_info_to_populate = user_info_to_populate)
# this route handles updating the user
@app.route('/update_user/<int:id>',methods=['POST'])
def update_user(id):
    # receiving data from the form and link them to the dictionary
    data = {
        'id': id,
        'first_name':request.form['firstname'],
        'last_name':request.form['lastname'],
        'email':request.form['email']
    }
    user.User.update_user(data)
    show_user_page_path = '/users/'+ str(id)
    return redirect(show_user_page_path)
# this route handles deleting the details of a single user
@app.route('/delete_user/<int:id>')
def delete_user(id):
    data = {
        'id':id
    }
    user.User.delete_user(data)
    return redirect ('/users')
# this route handles all the errors for resources not found
@app.errorhandler(404)
def errors(e):
    return render_template('error.html')