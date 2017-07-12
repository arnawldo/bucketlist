from flask import render_template, Blueprint

bucket_app = Blueprint('bucket', __name__)

@bucket_app.route("/home")
def home():
    return render_template("home.html")

@bucket_app.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@bucket_app.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
