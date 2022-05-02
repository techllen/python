from flask import Flask,render_template,redirect,request,session
import secrets
import random
import datetime
app = Flask(__name__)

# global variables
app.secret_key = secrets.token_hex()
activities = []

# index route
@app.route('/')
def home():
    # tatal all golds before rendering
    # gold_total = session['farm_gold_to_give'] + session['cave_gold_to_give'] + session['house_gold_to_give'] + session['casion_gold_to_give'] + session['casion_gold_to_take_away']
    # checking if all cookies exists and add all cookies that holds golds to the total
    if 'farm_gold_to_give' in session and 'cave_gold_to_give' not in session and 'house_gold_to_give' not in session and 'casino_gold_to_give_and_take_away' not in session:
        session['gold_total'] = int(session['farm_gold_to_give'])
    elif 'farm_gold_to_give' in session and 'cave_gold_to_give' in session and 'house_gold_to_give' not in session and 'casino_gold_to_give_and_take_away' not in session:
        session['gold_total'] = int(session['farm_gold_to_give']) + int(session['cave_gold_to_give'])
    elif 'farm_gold_to_give' in session and 'cave_gold_to_give' in session and 'house_gold_to_give' in session and 'casino_gold_to_give_and_take_away' not in session:
        session['gold_total'] = int(session['farm_gold_to_give'])+ int(session['cave_gold_to_give'])+ int(session['house_gold_to_give'])
    elif 'farm_gold_to_give' in session and 'cave_gold_to_give' in session and 'house_gold_to_give' in session and 'casino_gold_to_give_and_take_away' in session:
        session['gold_total'] = int(session['farm_gold_to_give'])+ int(session['cave_gold_to_give'])+ int(session['house_gold_to_give'])+ int(session['casino_gold_to_give_and_take_away'])
    return render_template('index.html')

# process money route
@app.route('/process_money' , methods = ['POST'])
def process_money():
    if request.form['form_type'] == 'farm':
        # generate random number if the form has been accessed
        session['farm_gold_to_give'] = random.randint(10,20)
        session['gold_total'] = + session['farm_gold_to_give']
        time = datetime.datetime.now()
        activity = ['win','Earned '+ str(session['farm_gold_to_give']) + ' golds from farm! ' +'('+ str((time))+')']
        activities.append(activity)
        
    elif request.form['form_type'] == 'cave':
        # generate random number if the form has been accessed
        session['cave_gold_to_give'] = random.randint(5,10)
        session['gold_total'] = session['cave_gold_to_give']
        time = datetime.datetime.now()
        activity = ['win','Earned '+ str(session['cave_gold_to_give']) + ' golds from cave! ' +'('+ str((time))+')']
        activities.append(activity)
        
    elif request.form['form_type'] == 'house':
        # generate random number if the form has been accessed
        session['house_gold_to_give'] = random.randint(2,5)
        session['gold_total'] = session['house_gold_to_give']
        time = datetime.datetime.now()
        activity = ['win','Earned '+ str(session['house_gold_to_give']) + ' golds from house! ' +'('+ str((time))+')']
        activities.append(activity)
    
    elif request.form['form_type'] == 'casino':
        # generate random number if the form has been accessed
        session['casino_gold_to_give_and_take_away'] = random.randint(0,50)
        # generating random events 1 for win and 2 for loss
        random_event = random.randint(1,2)
        # if a win event occur
        if random_event == 1:
            time = datetime.datetime.now()
            activity = ['win','Earned '+ str(session['casino_gold_to_give_and_take_away']) + ' golds from casino! ' +'('+ str((time))+')']
        # when a loss event occur
        elif random_event == 2:
            time = datetime.datetime.now()
            # session['casino_gold_to_give_and_take_away'] = - (session['casino_gold_to_give_and_take_away'])
            activity = ['loss','Entered a casino and lost '+ str(session['casino_gold_to_give_and_take_away']) + ' .....Ouch..... ' +'('+ str((time))+')']
        activities.append(activity) 
        
    session['activities'] = activities
    # + session['cave_gold_to_give'] 
    # + session['house_gold_to_give'] + session['casion_gold_to_give_and_take_away']        
    return redirect('/')

# reset
@app.route('/reset')
def restart_game():
    activities.clear()
    session.clear()
    return render_template('index.html')

# errorpage
@app.errorhandler(404)
def errors(e):
    return render_template('errors.html')

# debugging mode
if __name__ == '__main__':
    app.run(debug=True)