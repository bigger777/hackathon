from app import db


class Power_line(db.Model):
    __tablename__ = "Power_lines"
    id = db.Column(db.Integer,primary_key=True) #айди записи в таблицы 
    start_segment_name = db.Column(db.String(256)) #название стартового сегменат 
    end_segment_name = db.Column(db.String(256)) #название конечного сегмента 
    year_of_commissioning = db.Column(db.Integer) #год ввода в эксплуатуцию
    voltage_class = db.Column(db.String(256)) #класс напряжения
    technical_condition = db.Column(db.String(256)) #состояние сети (хорошо, удовлетворитель, в зоне риска)
    network_name = db.Column(db.String(256)) #наименование сети
    control_number = db.Column(db.String(256)) #диспетчерский номер ЛЭП
    lines_segments = db.relationship("Line_Segment") #ссылка на сегменты сети


class Line_Segment(db.Model):
    __tablename__ = "Lines_Segments"
    id = db.Column(db.Integer, primary_key=True) #айди записи в таблицы
    start_point = db.Column(db.String(256)) #название начального пункта сегмента
    end_point = db.Column(db.String(256)) #название конечного пункта сегмента
    segment_length = db.Column(db.Float) #длина проводов
    lines_amount = db.Column(db.Integer) #количество проводов
    wires_mark = db.Column(db.String(256)) #марка проводов 
    year_of_commissioning = db.Column(db.Integer) #год ввода в эксплуатацию
    wires_type = db.Column(db.String(256)) #кабельный участок или воздушная линия
    primary_line = db.Column(db.Boolean, nullable=False) #обозначение, является ли сегмент основной линией лэп или отпайкой (true если лэп, false если отпайка)
    power_line = db.relationship("Power_line") #ссылка на ЛЭП в которой этот сегмент находится
    power_line_id = db.Column(db.Integer, db.ForeignKey("Power_lines.id")) #связь с ключом хозяина
    control_number = db.Column(db.String(256)) #диспетчерский номер сегмента ЛЭП


class Substation(db.Model):
    __tablename__ = "Substations"
    id = db.Column(db.Integer, primary_key=True) #айди записи
    network_name = db.Column(db.String(256)) #наименования сети (ВРЭС БРЭС КРЭКС ПЕКС)
    substation_name = db.Column(db.String(256)) #название подстанции
    voltage_class = db.Column(db.String(256)) #класс напряжения
    year_of_commissioning = db.Column(db.Integer) #год ввода в эксплуатацию
    transformers = db.relationship("Transformer") #служебное поле отображающие связь с таблицей трансформаторов
    substation_number = db.Column(db.String(256)) #диспетчерский номер подстанции


class Transformer(db.Model):
    __tablename__ = "Transformers"
    id = db.Column(db.Integer, primary_key=True) #айди записи 
    substation_id = db.Column(db.Integer, db.ForeignKey("Substations.id")) #айди подстанции к которому трансформатор относится (связь с ключом хозяина)
    substation = db.relationship("Substation") #ссылка на подстанцию
    nominal_power = db.Column(db.Float) #номинальная мощность 
    year_manufacture = db.Column(db.Integer) #год изготовления
    year_activate = db.Column(db.Integer) #год включения (например на холостом ходу, вне включения в сеть)
    technical_condition = db.Column(db.String(256)) #состояние сети 
    transformer_type = db.Column(db.String(256)) #тип трансформатора
    transformer_number = db.Column(db.String(256)) #номер трансформатора 

