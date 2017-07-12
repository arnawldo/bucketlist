from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    manager.run()