from models import *

db.create_all()
pw = Power_line(year_of_commissioning = 1957, voltage_class = "110/10/6", technical_condition="годна")
db.session.add(pw)
ls = Line_Segment(start_point = "ПС Фабричная", end_point = "ГРЭС-03", segment_length=5.06, lines_amount=2, year_of_commissioning=1957, wires_type="АСУ-300 АС-300/39 АСО-300", power_line=pw)
db.session.add(ls)
db.session.commit()
