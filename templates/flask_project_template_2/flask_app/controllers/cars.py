from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models import user,car
from flask_app.controllers import users

# this route redirect users add a car page
@app.route("/new")
def new_car():
    # check if user is logged in
    if session.get("user_id")==None:
        return redirect("/")
    else:
        return render_template("new_car.html")
# this route saves a car to the database
@app.route("/save_car",methods = ["POST"])
def save_car():
    # check if user is logged in
    if session.get("user_id")==None:
        return redirect("/")
    else:
        # validate car inputs
        if car.Car.validate_car_inputs(request.form) == False:
            return render_template("new_car.html")
        else:
            car_data = {
                "price":request.form["price"],
                "model":request.form["model"],
                "make":request.form["make"],
                "year":request.form["year"],
                "description":request.form["description"],
                "id" : session["user_id"]
            }
            # save the car to the database
            car.Car.save_car(car_data)
            return redirect ("/dashboard")
# this method retrieves car from the database for edit
@app.route("/edit/<int:id>")
def get_car_for_editing(id):
     # check if user is logged in
    if session.get("user_id")==None: 
        return redirect("/")
    else: 
        data = {
            "id" : id,
        }
        return render_template ("edit_car.html",car_to_display = car.Car.get_one_car_by_id(data))
# this route update a car in a database
@app.route("/update",methods = ["POST"])
def update_car():
    # validating inputs from car form
    car_id = request.form["car_id"]
    if car.Car.validate_car_inputs(request.form) == False:
        return redirect(f"/edit/{car_id}")
    else:
        # getting all info from the edit form
        car_data = {
            "price":request.form["price"],
            "model":request.form["model"],
            "make":request.form["make"],
            "year":request.form["year"],
            "description":request.form["description"],
            "id" : request.form["car_id"]
        }
        car.Car.update_car(car_data)
        
    return redirect ("/dashboard")
# this route show car details
@app.route("/show/<int:id>")
def show_car(id):
    # check if user is logged in
    if session.get("user_id")==None: 
        return redirect("/")
    else: 
        car_data = {
            "id" : id
        }
        return render_template ("show_car.html",car_to_display = car.Car.get_one_car_with_user(car_data))
# this method delete car in the database
@app.route("/cars/delete/<int:id>")
def delete_car(id):
    data = {
        "id" : id
    }
    car.Car.delete_car(data)
    return redirect ("/dashboard")