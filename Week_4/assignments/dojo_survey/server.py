from flask import Flask,render_template,redirect, request,session
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_hex()
# index route
@app.route('/')
def home():
    return render_template('index.html')
# process route
@app.route('/process',methods = ['POST'])
def process_form():
    session['name'] = request.form['name']
    session['gender'] = request.form['gender']
    session['covidvaccinationstatus'] = request.form['covidvaccinationstatus']
    session['dojolocation'] = request.form['dojolocation']
    session['favoritelanguage'] = request.form['favoritelanguage']
    session['comments'] = request.form['comments']
    return redirect('/result')
# result route
@app.route('/result')
def result():
    return render_template('result.html')
# errors
@app.errorhandler(404)
def error(e):
    return render_template('error.html')
# debugging
if __name__ == "__main__":
    app.run(debug=True)