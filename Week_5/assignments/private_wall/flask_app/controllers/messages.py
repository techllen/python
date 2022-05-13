from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.controllers import users
from flask_app.models import message

# this route saves messages in the database
@app.route('/send_message',methods = ['POST'])
def send_message():
    # if message has allowed length save it
    if message.Message.message_is_valid(request.form['message']):
        data = {
            "content": request.form['message'],
            "sender_id": session['user_id'],
            "receiver_id":request.form["receiver_id"]
        }
        print(data)
        message.Message.save_message(data)
    # flash error message
    else:
        message.Message.message_is_valid(request.form['message'])
  
    return redirect ("/wall")