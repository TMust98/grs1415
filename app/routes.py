from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'John'}
    return render_template('index.html', title="Home", user=user)


@app.route('/login')
def login():
    return render_template('login.html')