from flask import Flask, render_template ,request
import joblib

app =Flask(__name__)
#firebase
import pyrebase
config = {
    "apiKey": "AIzaSyBhWoNgO2BXwf1dJAbvZOnEPnXYKMceT_I",
    "authDomain": "noticeboard-f5fbe.firebaseapp.com",
    "databaseURL": "https://noticeboard-f5fbe.firebaseio.com",
    "projectId": "noticeboard-f5fbe",
    "storageBucket": "noticeboard-f5fbe.appspot.com",
    "messagingSenderId": "443901202866",
    "appId": "1:443901202866:web:ee2b2ee32cf502dc6294ab",
    "measurementId": "G-0T14R4JR1E"
  }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('SB1') == 'SET':
            db.child("Boards").update({"board1":request.form['Board1']})
            print(request.form['Board1'])
        elif  request.form.get('SB2') == 'SET':
            db.child("Boards").update({"board2":request.form['Board2']})
            print(request.form['Board2'])
 
    return render_template("index.html")


if __name__ == '__main__':
    # port = int(os.environ.get("PORT", 5000))
    app.run()


     
   