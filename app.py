from flask import Flask, render_template, request
from database import get_database, connect_to_database


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/inserttask', methods=["POST", "GET"])
def inserttask():
    if request.method == "POST":
        #get the task entered by user from the form
        enteredtask = request.form['todaystask']
        db = get_database()
        db.execute("insert into todolist ( task) values (?)", ['enteredtask'])
        db.commit()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)