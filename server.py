from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "boonk gang"

from user_model import User

@app.route('/users/new')
def show_form():

    return render_template("form.html")

@app.route('/submit_user_form', methods = ['POST'])
def submit_user_form():

    User.add_user(request.form)

    return redirect('/users/')

@app.route("/users/")
def index():
    
    all_users = User.get_all()

    return render_template("index.html", all_users = all_users)



if __name__ == "__main__":
    app.run(debug=True)

