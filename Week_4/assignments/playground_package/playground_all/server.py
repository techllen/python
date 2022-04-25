from flask import Flask,render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:repeats>')
def repeat(repeats):
    return render_template('play.html', repeats = repeats)

@app.route('/play/<int:repeats>/<string:color>')
def play_color(repeats,color):
    return render_template('play.html', repeats = repeats,color = color)

if __name__=="__main__":
    app.run(debug=True)  