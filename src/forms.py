from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, RadioField

class Power_lineForm(FlaskForm):
    start_segment_name = StringField("Укажите название начального пункта ЛЭП (откуда)", [validators.InputRequired("Необходимо указать начальный пункт")])
    end_segment_name = StringField("Укажите название конечного пункта ЛЭП (куда)", [validators.InputRequired("Необходимо указать конечный пункт")])
    year_of_commissioning = IntegerField("Укажите год ввода ЛЭП в эксплуатацию", [validators.InputRequired("Необходимо указать год ввода в эксплуатацию")])
    voltage_class = StringField("Укажите класс напряжения", [validators.InputRequired("Необходимо указать класс напряжения")])
    technical_condition = StringField("Укажите техническое состояние ЛЭП", [validators.InputRequired("Необходимо указать техническое состояние ЛЭП")])
    network_name = StringField("Укажите наименование сети, к которой ЛЭП относится")
    control_number = StringField("Укажите диспетчерский номер ЛЭП", [validators.InputRequired("Необходимо указать диспетчерский номер ЛЭП")])


class Line_SegmentForm(FlaskForm):
    start_point = StringField("Укажите название начального пункта сегмента ЛЭП (откуда)", [validators.InputRequired("Необходимо указать пункт А для сегмента")])
    end_point = StringField("Укажите название конечного пункта сегмента ЛЭП (куда)", [validators.InputRequired("Необходимо указать пункт Б сегмента")])
    segment_length = IntegerField("Укажите год ввода сегмента ЛЭП в эксплуатацию", [validators.InputRequired("Необходимо указать год ввода в эксплуатацию")])
    lines_amount = IntegerField("Укажите количество линий сегмента ЛЭП", [validators.InputRequired("Необходимо указать количество линий")])
    wires_mark = StringField("Через символ | укажите марки проводов", [validators.InputRequired("Необходимо указать марки проводов")])
    year_of_commissioning = IntegerField("Укажите год ввода сегмента ЛЭП в эксплуатацию", [validators.InputRequired("Необходимо указать год ввода сегмента ЛЭП в эксплуатацию")])
    wires_type = StringField("Укажите техническое состояние ЛЭП", [validators.InputRequired("Необходимо указать техническое состояние ЛЭП")])
    network_name = StringField("Укажите наименование сети, к которой ЛЭП относится")
    control_number = StringField("Укажите диспетчерский номер сегмента ЛЭП", [validators.InputRequired("Необходимо указать диспетчерский номер сегмента ЛЭП")])


class SubstationForm(FlaskForm):
    network_name = StringField("Укажите наименование сети, к которой ЛЭП относится")
    substation_name = StringField("Укажите название подстанции", [validators.InputRequired("Необходимо указать название подстанции")])
    voltage_class = StringField("Укажите класс напряжения", [validators.InputRequired("Необходимо указать класс напряжения")])
    year_of_commissioning = IntegerField("Укажите год ввода подстанции в эксплуатацию", [validators.InputRequired("Необходимо указать год ввода подстанции в эксплуатацию")])


class TransformerForm(FlaskForm):
    nominal_power = IntegerField("Укажите номинальную мощность трансформатора", [validators.InputRequired("Необходимо номинальную мощность трансформатора")])
    year_manufacture = IntegerField("Укажите год производства трансформатора", [validators.InputRequired("Необходимо указать год производства трансформатора")])
    year_activate = IntegerField("Укажите год ввода трансформатора в эксплуатацию", [validators.InputRequired("Необходимо указать год ввода трансформатора в эксплуатацию")])
    technical_condition = StringField("Укажите техническое состояние трансформатора", [validators.InputRequired("Необходимо указать техническое состояние трансформатора")])
    transformer_type = StringField("Укажите тип трансформатора", [validators.InputRequired("Необходимо указать тип трансформатора")])
    transformer_number = StringField("Укажите диспетчерский номер трансформатора", [validators.InputRequired("Необходимо указать диспетчерский номер трансформатора")])

    
