from flask import Flask, render_template,request,redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    # row = Friend.create_friend()
    # Friend.update_friend()
    print(friends)
    return render_template("index.html",all_friends = friends)
            
# relevant code snippet from server.py
from friend import Friend
@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "occupation" : request.form["occ"]
        }
    Friend.create_friend(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

