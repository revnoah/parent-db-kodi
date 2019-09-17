from flask import render_template
from app import app
from app import mysql_connect
import os

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

# @app.route('/import')
# def index():
#     return render_template('import.html', title='Import From Main Database')

@app.route('/movies')
def movies():
    db = mysql_connect.Database()
    movies = db.dbMovies()

    return render_template('movies.html', title='Movies', movies=movies)
