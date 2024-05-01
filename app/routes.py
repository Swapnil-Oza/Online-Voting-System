from app import create_app
from app.models import User, Ballot
from flask import render_template, redirect, url_for

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login logic here
    return render_template('login.html')

@app.route('/ballot', methods=['GET', 'POST'])
def ballot():
    # Ballot logic here
    return render_template('ballot.html')

@app.route('/logout')
def logout():
    # Logout logic here
    return redirect(url_for('index'))
