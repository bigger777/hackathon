from app import db


class Power_line(db.Model):
    __tablename__ = "Power_lines"
    id = db.Column(db.Integer,primary_key=True) #айди записи в таблицы 
    start_segment_id = db.Column(db.String(50)) # айди стартового сегмента 
    start_segment_name = db.Column(db.String(256)) #название стартового сегменат 
    end_segment_id = db.Column(db.String(50)) #айди конечного сегмента 
    end_segment_name = db.Column(db.String(256)) #название конечного сегмента 
    year_of_commissioning = db.Column(db.Integer) #год ввода в эксплуатуцию
    voltage_class = db.Column(db.String(256)) #класс напряжения
    technical_condition = db.Column(db.String(256)) #состояние сети (хорошо, удовлетворитель, в зоне риска)
    network_name = db.Column(db.String(256)) #наименование сети

    lines_segments = db.relationship("Lines_Segments", back_populates="power_line") #ссылка на сегменты сети


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

    power_line = db.relationship("Power_lines", back_populates="lines_segments") #ссылка на ЛЭП в которой этот сегмент находится
    power_line_id = db.Column(db.Integer, db.ForeignKey("Power_lines.id")) #связь с ключом хозяина


class Substation(db.Model):
    __tablename__ = "Substations"
    id = db.Column(db.Integer, primary_key=True) #айди записи
    network_name = db.Column(db.String(256)) #наименования сети (ВРЭС БРЭС КРЭКС ПЕКС)
    substation_name = db.Column(db.String(256)) #название подстанции
    voltage_class = db.Column(db.String(256)) #класс напряжения
    year_of_commissioning = db.Column(db.Integer) #год ввода в эксплуатацию
    transformers = db.relationship("Transformers", back_populates="substation")


class Transformer(db.Model):
    __tablename__ = "Transformers"
    id = db.Column(db.Integer, primary_key=True) #айди записи 
    substation_id = db.Column(db.Integer, db.ForeignKey("Substations.id")) #айди подстанции к которому трансформатор относится (связь с ключом хозяина)
    substation = db.relationship("Substations", back_populates="transformers") #ссылка на подстанцию
    nominal_power = db.Column(db.Float) #номинальная мощность 
    year_manufacture = db.Column(db.Integer) #год изготовления
    year_activate = db.Column(db.Integer) #год включения (например на холостом ходу, вне включения в сеть)
    technical_condition = db.Column(db.String(256)) #состояние сети 
    transformer_type = db.Column(db.String(256)) #тип трансформатора
    transformer_number = db.Column(db.String(256)) #номер трансформатора 

