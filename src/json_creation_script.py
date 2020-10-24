import json

data = {
        1 : {
            "start_segment_name" : "Мебельная",
            "end_segment_name" : "Фабричная",
            "year_of_commissioning" : 1957,
            "voltage_class" : 110, 
            "technical_condition" : "годна",
            "network_name" : "", 
            "control_number" : "А-1/2",
            "lines_segments" : {
                    0 : {
                        "start_point" : "ПС Мебельная",
                        "end_point" : "отп.оп. на ПС 1",
                        "segment_length" : 4.8473,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1957,
                        "wires_mark" : "АСУ-300|АСО-300",
                        "primary_line" : True
                        },
                    1 : {
                        "start_point" : "отп. на ПС 1",
                        "end_point" : "",
                        "segment_length" : 1.398,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1957,
                        "wires_mark" : "АПС-150/24",
                        "primary_line" : False
                        },
                    2 : {
                        "start_point" : "отп.оп. на ПС 1",
                        "end_point" : "отп.оп. на ПС 2",
                        "segment_length" : 3.5607,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1957,
                        "wires_mark" : "АСУ-300|AC-300/39",
                        "primary_line" : True
                        },
                    3 : {
                        "start_point" : "отп. на ПС 2",
                        "end_point" : "",
                        "segment_length" : 1.2453,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1957,
                        "wires_mark" : "АС-150",
                        "primary_line" : False
                        },
                    4 : {
                        "start_point" : "отп.оп. на ПС 2",
                        "end_point" : "отп.оп. на ПС 3",
                        "segment_length" : 2.243,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1957,
                        "wires_mark" : "АС-300/39",
                        "primary_line" : True
                        },
                    5 : {
                        "start_point" : "отп.на ПС 3",
                        "end_point" : "",
                        "segment_length" : 0.444,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1957,
                        "wires_mark" : "АС-185",
                        "primary_line" : False
                        },
                    6 : {
                        "start_point" : "отп.оп. на ПС 3",
                        "end_point" : "Фабричная",
                        "segment_length" : 0.8461,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1957,
                        "wires_mark" : "АС-300/39",
                        "primary_line" : True
                        }
                }
            }, 
        2 : {
            "start_segment_name" : "ПС Фабричная",
            "end_segment_name" : "ГРЭС-03",
            "year_of_commissioning" : 1957,
            "voltage_class" : 110, 
            "technical_condition" : "годна",
            "network_name" : "", 
            "control_number" : "А-3/4",
            "lines_segments" : {
                0 : {
                        "start_point" : "ПС Фабричная",
                        "end_point" : "ГРЭС-03",
                        "segment_length" : 5.05523,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1957,
                        "wires_mark" : "АСУ-300|АСУ-300/39|АС0-300",
                        "primary_line" : True
                    }  
                }
            },
        3 : {
            "start_segment_name" : "ГРЭС-03",
            "end_segment_name" : "ТЭЦ-1",
            "year_of_commissioning" : 1951,
            "voltage_class" : 110, 
            "technical_condition" : "годна",
            "network_name" : "", 
            "control_number" : "А-5/6",
            "lines_segments" : {
                0 : {
                        "start_point" : "ГРЭС-03",
                        "end_point" : "ТЭЦ-1",
                        "segment_length" : 1.8645,
                        "lines_amount" : 2,
                        "year_of_commissioning" : 1951,
                        "wires_mark" : "АСУ-300|АСУ-300/39",
                        "primary_line" : True
                    }
                }
            }
        }

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
