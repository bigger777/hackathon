from flask import render_template, redirect, url_for, abort
from app import app, db
from forms import *
from models import *


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/edit/<object>/<id>/")
def edit(object, id):
    return render_template("edit.html")

@app.route("/add/")
def add():
    return render_template("add.html")

@app.route("/download/")
