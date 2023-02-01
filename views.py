from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    print('rendering: home')
    return render_template("index.html",name = "Fernando")

@views.route("/about")
def aboutme():
    print('rendering: home')
    return render_template("about.html",name = "Fernando")