from flask import Flask
app = Flask(__name__)

# localhost:5000/ - have it say "Hello World!"
@app.route('/') 
def hello():
    return 'Hello World'

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
@app.route('/say/<string:word>')
def say_hi(word):
    return 'Hi ' + word 

# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<int:number_of_repeations>/<string:word>')
def repeat(number_of_repeations,word):
    for round in range(number_of_repeations):
        return word
