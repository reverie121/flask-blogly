"""Blogly application."""

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = "do*not*tell"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

debug = DebugToolbarExtension(app)

@app.route("/")
def main():
    """ TBD. Redirects to user list at the moment. """

    return redirect('/users')

@app.route("/users")
def list_users():
    """ Show a list of all users. """

    users = User.query.all()
    return render_template("user-list.html", users=users)

@app.route("/users/new")
def new_user_form():
    """Show an add form for new users."""

    users = User.query.all()
    return render_template("new-user-form.html", users=users)

@app.route("/users/new", methods=['POST'])
def new_user_form_submit():
    """Process the add user form, adding a new 
    user to db and redirecting to user list."""

    first_name = request.form['first-name']
    last_name = request.form['last-name']
    image_url = request.form['image-url'] or None

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(user)
    db.session.commit()

    return redirect(f"/users/{user.id}")

@app.route("/users/<user_id>")
def show_user(user_id):
    """ Show information about the user with corresponding id. """
    user = User.query.get_or_404(user_id)
    return render_template("user-details.html", user=user)

@app.route("/users/<user_id>/edit")
def edit_user(user_id):
    """ Show an edit user form. """
    user = User.query.get_or_404(user_id)
    return render_template("user-edit.html", user=user)

@app.route("/users/<user_id>/edit", methods=["POST"])
def show_edit_user_form(user_id):
    """ Update database based on user submission 
    and show updated user details. """
    user = User.query.get_or_404(user_id)

    user.first_name = request.form['first-name']
    user.last_name = request.form['last-name']
    user.image_url = request.form['image-url']

    db.session.add(user)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route("/users/<user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """ Delete the user with corresponding id. """
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')