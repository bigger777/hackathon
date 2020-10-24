from models import *
import json

with open("data_file.json", 'r') as read_file:
    data = json.load(read_file)

db.create_all()
for index, value in data.items():
    pl = Power_line()
    for key, e in value.items():
        if key == "start_segment_name":
            pl.start_segment_name = e
        if key == "end_segment_name":
            pl.end_segment_name = e
        if key == "year_of_commissioning":
            pl.year_of_commissioning = e
        if key == "voltage_class":
            pl.voltage_class = e
        if key == "technical_condition":
            pl.technical_condition = e
        if key == "control_number":
            pl.control_number = e
        if key == "lines_segments":
            db.session.add(pl)
            for line in e.values():
                ls = Line_Segment()
                for key, value in line.items():
                    if key == "start_point":
                        ls.start_point = value
                    if key == "end_point":
                        ls.end_point = value
                    if key == "segment_length":
                        ls.segment_length = value
                    if key == "lines_amount":
                        ls.lines_amount = value
                    if key == "year_of_commissioning": 
                        ls.year_of_commissioning = value
                    if key == "wires_mark":
                        ls.wires_mark = value
                    if key == "primary_line":
                        ls.primary_line = value
                    ls.power_line_id = index
                    db.session.add(ls)

db.session.commit()
