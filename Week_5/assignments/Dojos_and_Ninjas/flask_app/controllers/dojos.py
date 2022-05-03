from flask_app import app
from flask import render_template,request,redirect
from flask_app.models import dojo

# this route will redirect users to the dojo page
@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    all_dojos = dojo.Dojo.view_dojos()
    return render_template('/dojos.html',all_dojos = all_dojos)

@app.route('/show_ninjas/<int:id>')
def show_ninjas(id):
    data = {
        'id':id
    }
    dojo_results = dojo.Dojo.show_ninjas(data);
    # we can pick the name from any element because the name is the same throughout the result set
    return render_template('/dojo_show.html',dojo = dojo_results)

@app.route('/add_dojo',methods=['POST'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    dojo.Dojo.save_dojo(data)
    return redirect('/')
    
    
    
    
    
