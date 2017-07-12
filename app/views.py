from flask import render_template, Blueprint

bucket = Blueprint('bucket', __name__)

@bucket.route("/home")
def home():
    return render_template("home.html")

@bucket.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@bucket.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

