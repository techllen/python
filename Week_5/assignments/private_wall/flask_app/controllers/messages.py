from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.controllers import users
from flask_app.models import message

# this route saves messages in the database
@app.route('/send_message',methods = ['POST'])
def send_message():
    # if message has allowed length save it
    valid_message = message.Message.validate_message(request.form)
    # save data if message is valid
    if valid_message == True: 
        data = {
                "content": request.form['message'],
                "sender_id": session['user_id'],
                "receiver_id":request.form["receiver_id"]
            }
        message.Message.save_message(data)
    return redirect ("/wall")

@app.route("/delete_message",methods = ["POST"])
def delete_message():
    data = {
        "id" : request.form["message_id"]
    }
    # call delete message from model
    message.Message.delete_message(data)
    return redirect ("/wall")
