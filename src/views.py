from flask import render_template, redirect, url_for, abort
from app import app
from forms import *
from models import *


names_goals = {"Таблица ЛЭП" : "power_line", "Таблица сегментов сети" : "line_segment", "Таблица подстанций" : "substation", "Таблица трансформаторов" : "transformer"}
goals_names = {"power_line":"Таблица ЛЭП","line_segment":"Таблица сегментов сети","substation":"Таблица подстанций","transformer":"Таблица трансформаторов"}
goals_models = {"power_line":"Power_line","line_segment":"Line_Segment","substation":"Substation","transformer":"Transformer"}
goals_forms = {"power_line":"Power_lineForm","line_segment":"Line_SegmentForm","substation":"SubstationForm","transformer":"TransformerForm"}

@app.route("/")
def index():
    power_lines = db.session.query(Power_line).all()
    lines_segments = db.session.query(Line_Segment).all()
    substations = db.session.query(Substation).all()
    transformers = db.session.query(Transformer).all()
    return render_template("index.html", goals_names=goals_names, power_lines=power_lines, lines_segments=lines_segments, substations=substations, transformers=transformers)

@app.route("/edit/<obj>/<id>/")
def edit(obj, id):
    if obj not in goals_names.keys():
        abort(404)
    obj = db.session.query(obj).get_or_404(id)


    return render_template("edit.html")

@app.route("/add/")
def add():
    return render_template("add.html")

@app.route("/add/<obj>/")
def add_spec(obj):
    if obj == "power_line":
        form = Power_lineForm
    elif obj == "line_segment":
        form = Line_SegmentForm
    elif obj == "substation":
        form = SubstationForm
    elif obj == "transformer":
        form = TransformerForm
    for e in form:
        print(e)
    return render_template("add_spec.html", form=form)

@app.route("/download/")
def download():
    return render_template("download.html")
