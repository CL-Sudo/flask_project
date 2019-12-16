from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Phil'}
    posts = [
        {
            "author": {"username": "John", "gender":"male"},
            "body": "Beautiful day in Portland!"
        },

        {
            "author": {"username": "Susan", "gender":"female"},
            "body": "The movie was so damn cool!"
        }
    ]
    return render_template("index.html", 
                            title = "Home", 
                            user = user, 
                            posts = posts)