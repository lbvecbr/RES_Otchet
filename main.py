# !/usr/bin/env python
# -*- coding: utf-8 -*-
from mInitial_Data import data
from docxtpl import DocxTemplate


data.filling_dicts()
doc = DocxTemplate(data.file_res_template)
context = data.make_dict()
print(context)
doc.render(context)
doc.save(data.file_generated)

answer = input('Do you want to replace prev_readings_file(y/n)')
if answer == 'y':
    f = open(data.file_now_readings)
    now_readings = f.read()
    f.close()

    f = open(data.file_prev_readings, 'w')
    f.write(now_readings)
    f.close()
    print('Replaced')
else:
    print('Canceled')







