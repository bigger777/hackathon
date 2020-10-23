from flask import render_template
from app import app, db
from forms import *
from models import *


@app.route("/", methods=["GET", "POST"])
def index():
    form = UserForm()
    if form.validate_on_submit():
        db.session.add(User(name=form.name.data))
        db.session.commit()
    users = db.session.query(User).all()
    return render_template("index.html", form=form, users=users)