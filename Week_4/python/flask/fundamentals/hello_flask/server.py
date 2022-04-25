import re
from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    # return 'Hello World!'  # Return the string 'Hello World!' as a response
    return render_template('index.html')

@app.route('/seccess')
def seccess():
    return 'Success'

@app.route('/hello/<string:name>/<int:repeats>')
def hello(name,repeats):
    # return "Hello  " + name
    return render_template('hello.html',name = name,repeats = repeats)

@app.route('/identify/<string:name>/<int:id>')
def identify(name,id):
    return "Hello  " + name + " of " + str(id)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

