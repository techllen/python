from flask_app import app
from flask import render_template,request,redirect
from flask_app.models import ninja,dojo

@app.route('/ninjas')
def ninjas():
    all_dojos = dojo.Dojo.view_dojos()
    return render_template('/new_ninja.html',all_dojos = all_dojos)

@app.route('/add_ninja',methods = ['POST'])
def add_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    ninja.Ninja.add_ninja(data)
    return redirect('/')