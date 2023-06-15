from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "boonk gang"

from user_model import User

@app.route('/')
def sendtousers():
    return redirect('/users')

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

@app.route('/users/<int:user_id>/')
def show_user(user_id):
    
    one_user = User.get_one({'user_id' : user_id})

    return render_template('show.html', one_user = one_user)

@app.route('/users/<int:user_id>/edit/')
def show_edit_form(user_id):

    one_user = User.get_one({'user_id' : user_id})

    return render_template('edit_form.html', one_user=one_user)

@app.route('/edit_users', methods = ['POST'])
def edit_user():
    
    User.update_user(request.form)

    return redirect('/users/')

@app.route('/delete/<int:user_id>/')
def deletus_user(user_id):

    User.delete_user({'user_id' : user_id})

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

