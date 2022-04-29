from flask import Flask,render_template,redirect, request,session
import secrets
import base64
app = Flask(__name__)
app.secret_key = secrets.token_hex()

# Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
# index route
@app.route('/')
def show_counter():
    # printing the key in hex format
    print(app.secret_key)
    # checking if we have a count in session and add one to it
    if 'count' in session:
        session['count'] += 1
    # with no count in session we will put it as one because its the first time
    else:
        session['count'] = 1    
    return render_template('index.html',count = session['count'])

# Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
# clear route
@app.route('/destroy_session')
def destroy_session():
    # getting rid of everything currently whats stored in session
    session.clear()
    return redirect('/')


# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
# increment by 2 route
@app.route('/increment_by_2')
def increment_by_2():
    session['count'] +=2
    return render_template('index.html',count = session['count'])

# NINJA BONUS: Add a Reset button to reset the counter
# reset counter
@app.route('/reset_counter')
def reset_counter():
    session.pop('count',None)
    return redirect('/')

# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
# increment using form
@app.route('/increment_form',methods = ['POST'])
def increment_using_form():
    session['count'] += int(request.form['increment'])        
    return redirect('/')

# errors
@app.errorhandler(404)
def error(e):
    return render_template('error.html')

# decoding cookie
# pring count cookies on console
print(base64.urlsafe_b64decode('eyJjb3VudCI6Mn0==='))


# Run the app
if __name__ == '__main__':
    app.run(debug=True)