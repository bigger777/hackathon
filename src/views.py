from flask import render_template, redirect, url_for, abort, request
from app import app
from forms import *
from models import *


names_goals = {"Таблица ЛЭП" : "power_line", "Таблица сегментов сети" : "line_segment", "Таблица подстанций" : "substation", "Таблица трансформаторов" : "transformer"}
goals_names = {"power_line":"Таблица ЛЭП","line_segment":"Таблица сегментов сети","substation":"Таблица подстанций","transformer":"Таблица трансформаторов"}
goals_models = {"power_line":Power_line,"line_segment":Line_Segment,"substation":Substation,"transformer":Transformer}
goals_forms = {"power_line":Power_lineForm,"line_segment":Line_SegmentForm,"substation":SubstationForm,"transformer":TransformerForm}

@app.route("/")
def index():
    power_lines = db.session.query(Power_line).all()
    lines_segments = db.session.query(Line_Segment).all()
    substations = db.session.query(Substation).all()
    transformers = db.session.query(Transformer).all()
    return render_template("index.html", goals_names=goals_names, power_lines=power_lines, lines_segments=lines_segments, substations=substations, transformers=transformers)

@app.route("/edit/<obj>/<index>/", methods=['GET', 'POST'])
def edit(obj, index):
    if obj not in goals_names.keys():
        abort(404)
    objM = db.session.query(goals_models[obj]).get_or_404(index)
    form = (goals_forms[obj])(obj=objM)
    if request.method == 'POST' and form.validate_on_submit():
        if obj == "power_line":
            objM.start_segment_name = form.start_segment_name.data
            objM.end_segment_name = form.end_segment_name.data
            objM.year_of_commissioning = form.year_of_commissioning.data
            objM.voltage_class = form.voltage_class.data
            objM.technical_condition = form.technical_condition.data
            objM.network_name = form.network_name.data
            objM.control_number = form.control_number.data
        elif obj == "line_segment":
            objM.start_point = form.start_point.data
            objM.end_point = form.end_point.data
            objM.segment_length = form.segment_length.data
            objM.lines_amount = form.lines_amount.data
            objM.wires_mark = form.wires_mark.data
            objM.year_of_commissioning = form.year_of_commissioning.data
            objM.wires_type = form.wires_type.data
            objM.primary_line = form.primary_line.data
            objM.control_number = form.control_number.data
        elif obj == "substation":
            objM.network_name = form.network_name.data
            objM.substation_name = form.substation_name.data
            objM.voltage_claobjM = form.voltage_claobjM.data
            objM.year_of_commiobjMioning = form.year_of_commiobjMioning.data
            objM.substation_number = form.substation_number.data
        elif obj == "transformer":
            objM.substation_id = form.substation_id.data
            objM.nominal_power = form.nominal_power.data
            objM.year_manufacture = form.year_manufacture.data
            objM.year_activate = form.year_activate.data
            objM.technical_condition = form.technical_condition.data
            objM.transformer_type = form.transformer_type.data
            objM.transformer_number = form.transformer_number.data
        db.session.commit()
        return redirect(url_for('index'))


    return render_template("edit.html", form=form, obj=obj)

@app.route("/add/")
def add():
    return render_template("add.html")

@app.route("/delete/<obj>/<index>/")
def delete(obj, index):
    if obj not in goals_names.keys():
        abort(404)
    objM = db.session.query(goals_models[obj]).get_or_404(index)
    db.session.delete(objM)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/add/<obj>/", methods=['GET', 'POST'])
def add_spec(obj):
    form = (goals_forms[obj])()
    if request.method == 'POST' and form.validate_on_submit():
        if obj == "power_line":
            pl = Power_line()
            pl.start_segment_name = form.start_segment_name.data
            pl.end_segment_name = form.end_segment_name.data
            pl.year_of_commissioning = form.year_of_commissioning.data
            pl.voltage_class = form.voltage_class.data
            pl.technical_condition = form.technical_condition.data
            pl.network_name = form.network_name.data
            pl.control_number = form.control_number.data
            db.session.add(pl)
        elif obj == "line_segment":
            ls = Line_Segment()
            ls.start_point = form.start_point.data
            ls.end_point = form.end_point.data
            ls.segment_length = form.segment_length.data
            ls.lines_amount = form.lines_amount.data
            ls.wires_mark = form.wires_mark.data
            ls.year_of_commissioning = form.year_of_commissioning.data
            ls.wires_type = form.wires_type.data
            ls.primary_line = form.primary_line.data
            ls.control_number = form.control_number.data
            db.session.add(ls)
        elif obj == "substation":
            ss = Substation()
            ss.network_name = form.network_name.data
            ss.substation_name = form.substation_name.data
            ss.voltage_class = form.voltage_class.data
            ss.year_of_commissioning = form.year_of_commissioning.data
            ss.substation_number = form.substation_number.data
            db.session.add(ss)
        elif obj == "transformer":
            tf = Transformer()
            tf.substation_id = form.substation_id.data
            tf.nominal_power = form.nominal_power.data
            tf.year_manufacture = form.year_manufacture.data
            tf.year_activate = form.year_activate.data
            tf.technical_condition = form.technical_condition.data
            tf.transformer_type = form.transformer_type.data
            tf.transformer_number = form.transformer_number.data
            db.session.add(tf)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add_spec.html", form=form, obj=obj)

@app.route("/download/")
def download():
    return render_template("download.html")
