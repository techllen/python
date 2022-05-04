from flask_app import app
from flask import render_template,request,redirect
from flask_app.models import ninja,dojo
from flask_app.controllers import dojos

# this route brings all the dojos to the new ninja page
@app.route('/ninjas')
def ninjas():
    all_dojos = dojo.Dojo.view_dojos()
    return render_template('/new_ninja.html',all_dojos = all_dojos)
# this route adds ninjas to the database
@app.route('/add_ninja',methods = ['POST'])
def add_ninja():
    dojo_id = request.form['dojo_id']
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : dojo_id
    }
    # make the path into string format
    show_ninja_path = '/show_ninjas/'+str(dojo_id)
    ninja.Ninja.add_ninja(data)
    # redirecting to the page that show all ninjas in a particular dojo
    return redirect(show_ninja_path)