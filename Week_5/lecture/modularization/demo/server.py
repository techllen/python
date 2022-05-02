# import app
from flask_app import app
# import all controllers
from flask_app.controllers import inventories,users
# run the app in debug mode
if __name__=="__main__": 
    app.run(debug=True)