from flask import Flask
app = Flask(__name__)

# localhost:5000/ - have it say "Hello World!"
@app.route('/') 
def hello():
    return 'Hello World!'

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
#  Ensure the names provided in the 3rd task are strings
@app.route('/say/<string:word>')
def say_hi(word):
    return 'Hi ' + word +'!'

# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string
@app.route('/repeat/<int:number_of_repeations>/<string:word>')
def repeat(number_of_repeations,word):
    # return printing(word,number_of_repeations)
    words = {1:'key'}
    for round in range(number_of_repeations):
        words.update({round,word})
    return words
    

# A function to return the value we wanna print
# def printing(phrase,repeations):
#     for round in range(repeations):
#         print(str(round) + phrase ) 
#         return str(round) + phrase 
    
# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."
@app.errorhandler(404)
def error():
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True)  

# def test():
#     return printing('dogs',35)

# print(test())