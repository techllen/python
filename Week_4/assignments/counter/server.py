from flask import Flask,render_template,redirect, request,session
import secrets
import base64
app = Flask(__name__)
app.secret_key = secrets.token_hex()

# Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
# index route
total = 0
@app.route('/')
def show_counter():
    # printing the key in hex format
    # print(app.secret_key)
    # checking if we have a count in session and add one to it
    if 'count' in session:
        session['count'] += 1
    # with no count in session we will put it as one because its the first time
    else:
        session['count'] = 0    
    #checking if cookies exists and add them to the total
    if 'increment_by_two' in session and 'increments' not in session:
        total = int(session['count']) + int(session['increment_by_two'])
    elif 'increments' in session and 'increment_by_two' not in session:
        total = int(session['count']) + int(session['increments'])
    elif ('increment_by_two' in session) and ('increments' in session):
        total = int(session['count']) + int(session['increment_by_two']) + int(session['increments'])
    else:
        total = session['count']
    session['total'] = total    
    return render_template('index.html')

# Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
# clear route
@app.route('/destroy_session')
def destroy_session():
    # getting rid of everything currently stored in the session
    session.clear()
    return redirect('/')


# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
# increment by 2 route
@app.route('/increment_by_two')
def increment_by_two():
    if 'increment_by_two' not in session:
        session['increment_by_two'] = 2
    else:
        session['increment_by_two'] += 2 
    return redirect('/') 

# NINJA BONUS: Add a Reset button to reset the counter
# reset counter
@app.route('/reset_counter')
def reset_counter():
    session.pop('count')
    if 'increments' in session:
        session.pop('increments')
    if 'increments_by_2' in session:
        session.pop('increment_by_two')
    if 'total' in session:
        session.pop('total')
    session.clear()
    return redirect('/')

# SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
# increment using form
@app.route('/increment_form',methods = ['POST'])
def increment_using_form():
    increment = int(request.form['increment'])
    if 'increments' not in session:
        session['increments'] = increment
    else:
        session['increments'] += increment
    return redirect('/')

# errors
@app.errorhandler(404)
def error(e):
    return render_template('error.html')

# decoding cookie
# pring count cookies on console
print(base64.urlsafe_b64decode('eyJjb3VudCI6Mn0==='))

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)