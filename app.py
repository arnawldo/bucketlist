from app import create_app
from flask_script import Manager
from flask import render_template, Blueprint, request, session, redirect, url_for, flash

from app.decorators import requires_login
from app.exceptions import UserNotExistsError, IncorrectPasswordError, UserAlreadyExistsError
from app.forms import LoginForm, RegistrationForm, NewBucketForm
from app.models import User, Database, BucketList

from app.models import Database

db = Database()
app = create_app('default')






@app.route("/")
def home():
    return render_template("home.html")

# @app.app_errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
#
# @app.app_errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    bucket_form = NewBucketForm()
    if form.validate_on_submit():
        try:
            is_user_valid = db.verify_login_credentials(email=form.email.data, password=form.password.data)
            if is_user_valid:
                session['email'] = form.email.data
                user = db.find_user_by_email(form.email.data)
                return redirect("/buckets")
            flash("Invalid username or password")
        except UserNotExistsError:
            flash("User {} does not exist!".format(form.email.data))


    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    password=form.password.data)
        try:
            db.insert_user(user)
            flash('You are registered.')
            return redirect(url_for('login'))
        except UserAlreadyExistsError:
            flash("User already exists")
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    session['email'] = None
    return redirect(url_for('home'))

@app.route('/buckets', methods=["GET", "POST"])
@requires_login
def buckets():
    user = db.find_user_by_email(session["email"])
    return render_template("buckets.html", user=user)

@app.route('/create_bucket', methods=["GET", "POST"])
def create_bucket():
    form = NewBucketForm()
    if form.validate_on_submit():
        user = db.find_user_by_email(session["email"])
        user.create_bucket_list(form.name.data, form.description.data)
        return redirect(url_for("buckets"))
    user = db.find_user_by_email(session["email"])
    return render_template("create_bucket.html", form=form)

# @app.route('/delete/<string:alert_id>')
# @requires_login
# def delete_bucket(bucket_name):
#     user = db.find_user_by_email(session["email"])
#     user.d
#     return redirect(url_for('users.user_alerts'))

if __name__ == '__main__':
    app.run(debug=True)