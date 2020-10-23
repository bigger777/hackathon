from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class power_line(db.Model):
    __tablename__ = "power_lines"
    id = db.Column(db.Integer,primary_key=True) #айди записи в таблицы 
    start_segment_id = db.Column(db.String(50)) # айди стартового сегмента 
    start_segment_name = db.Column(db.String(256),nullable=False) #название стартового сегменат 
    end_segment_id = db.Column(db.String(50),nullable=False) #айди конечного сегмента 
    end_segment_name = db.Column(db.String(256),nullable=False) #название конечного сегмента 
    year_of_commissioning = db.Column(db.Integer) #год ввода в эксплуатуцию
    voltage_class = db.Column(db.String(256)) #класс напряжения
    technical_condition = db.Column(db.String(256)) #состояние сети (хорошо, удовлетворитель, в зоне риска)
    network_name = db.Column(db.String(256)) #наименование сети

    lines_segments = db.relationship("line_segment") #ссылка на сегменты сети


class line_segment(db.Model):
    __tablename__ = "lines_segments"
    id = db.Column(db.Integer, primary_key=True) #айди записи в таблицы
    start_point = db.Column(db.String(256)) #название начального пункта сегмента
    end_point = db.Column(db.String(256)) #название конечного пункта сегмента
    segment_length = db.Column(db.Integer) #длина проводов
    lines_amount = db.Column(db.Integer) #количество проводов
    wires_mark = db.Column(db.String(256)) #марка проводов 
    year_of_commissioning = db.Column(db.Integer) #год ввода в эксплуатацию
    wires_type = db.Column(db.String(256)) #кабельный участок или воздушная линия

    power_line = db.relationship("power_line") #ссылка на ЛЭП в которой этот сегмент находится
    power_line_id = db.Column(db.Integer, db.ForeignKey("Power_Line.id")) #связь с ключом хозяина


class substation(db.Model):
    __tablename__ = "substations"
    id = db.Column(db.Integer, primary_key=True) #айди записи
    network_name = db.Column(db.String(256)) #наименования сети (ВРЭС БРЭС КРЭКС ПЕКС)
    substation_name = db.Column(db.String(256)) #название подстанции
    voltage_class = db.Column(db.String(256)) #класс напряжения
    year_of_commissioning = db.Column(db.Integer) #год ввода в эксплуатацию
    transformers = db.relationship("transformer")


class transformer(db.Model):
    __tablename__ = "transformers"
    id = db.Column(db.Integer, primary_key=True) #айди записи 
    substation_id = db.Column(db.Integer, db.ForeignKey("substation.id")) #айди подстанции к которому трансформатор относится (связь с ключом хозяина)
    substation = db.relationship("substation") #ссылка на подстанцию
    nominal_power = db.Column(db.Integer) #номинальная мощность 
    year_manufacture = db.Column(db.Integer) #год изготовления
    year_activate = db.Column(db.Integer) #год включения (например на холостом ходу, вне включения в сеть)
    technical_condition = db.Column(db.String(256)) #состояние сети 
    transformer_type = b.Column(db.String(256)) #тип трансформатора

