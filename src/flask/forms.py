from flask_wtf import FlaskForm
from wtforms import StringField, validators


class UserForm(FlaskForm):
    name = StringField("name", [validators.InputRequired(
        message="Необходимо указать имя. ")])
