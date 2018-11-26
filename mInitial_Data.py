# !/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import os.path


class Initial_Data(object):
    def __init__(self):
        self.file_now_readings = os.path.join(os.getcwd(), 'result_files', 'now_readings.txt')
        self.file_prev_readings = os.path.join(os.getcwd(), 'result_files', 'prev_readings.txt')
        self.file_res_template = os.path.join(os.getcwd(), 'result_files', 'res_template.docx')
        self.file_generated = os.path.join(os.getcwd(), 'result_files', 'generated.docx')
        self.file_gistogram_png = os.path.join(os.getcwd(), 'result_files', 'gistogram.png')
        self.file_gistogram_svg = os.path.join(os.getcwd(), 'result_files', 'gistogram.svg')

        f = open(self.file_prev_readings, 'r')
        self.prev_readings = eval(f.read())
        f.close()

        self.now_readings = {'grigorivske': 0, 'common': 0, 'komplex': 0, 'mtf': 0,
                        'tik': 0, 'maisterna': 0, 'tr.br1': 0, 'stf': 0, 'str.ceh': 0,
                        'zernosklad': 0, 'tr.br3': 0, 'kontora': 0, 'lotok': 0}

        self.coeficients = {'grigorivske': 1, 'common': 30, 'komplex': 1, 'mtf': 1,
                        'tik': 60, 'maisterna': 1, 'tr.br1': 1, 'stf': 1, 'str.ceh': 1,
                        'zernosklad': 1, 'tr.br3': 1, 'kontora': 1, 'lotok': 1}

        self.difference = {'grigorivske': 0, 'common': 0, 'komplex': 0, 'mtf': 0,
                        'tik': 0, 'maisterna': 0, 'tr.br1': 0, 'stf': 0, 'str.ceh': 0,
                        'zernosklad': 0, 'tr.br3': 0, 'kontora': 0, 'lotok': 0}

        self.amount = {'grigorivske': 0, 'common': 0, 'komplex': 0, 'mtf': 0,
                        'tik': 0, 'maisterna': 0, 'tr.br1': 0, 'stf': 0, 'str.ceh': 0,
                        'zernosklad': 0, 'tr.br3': 0, 'kontora': 0, 'lotok': 0}


        self.months = ['', 'січень', 'лютий', 'березень', 'квітень', 'травень', 'червень',
                  'липень', 'серпень', 'вересень', 'жовтень', 'листопад', 'грудень']

        self.months1 = ['', 'січня', 'лютого', 'березня', 'квітня', 'травня', 'червня',
                  'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня']

        self.result = 0


    def filling_dicts(self):
        f = open(self.file_now_readings, 'r')
        self.now_readings = eval(f.read())
        f.close()
        answer = input('Du you want to input now_readings(y/n)')
        if self.now_readings['tik'] == 0 or self.now_readings['tik'] == self.prev_readings['tik'] or answer == 'y':
            for K in self.now_readings.keys():
                if K != 'komplex':
                    self.now_readings[K] = int(input(K + ' <<<  '))
                else : self.now_readings[K] = 0
            f = open(self.file_now_readings, 'w')
            f.write(repr(self.now_readings))
            f.close()

        for Key in self.difference.keys():
            self.difference[Key] = self.now_readings[Key] - self.prev_readings[Key]
            self.amount[Key] = self.difference[Key] * self.coeficients[Key]
            self.result += self.amount[Key]
        self.result -= self.amount['grigorivske']
        self.amount['komplex'] = self.amount['common'] - self.amount['grigorivske']

    def make_dict(self):
        dict = {}

        date = datetime.now()
        dict_month = {'month': self.months[date.month], 'month1': self.months1[date.month]}
        dict_year = {'year': date.year}

        dict_now = {'n' + str(i): K for i, K in enumerate(self.now_readings.values())}
        dict_prev = {'p' + str(i): K for i, K in enumerate(self.prev_readings.values())}
        dict_raznica = {'s' + str(i): K for i, K in enumerate(self.difference.values())}
        dict_amount = {'c' + str(i): K for i, K in enumerate(self.amount.values())}

        dict.update(dict_amount)
        dict.update(dict_raznica)
        dict.update(dict_now)
        dict.update(dict_prev)
        dict.update({'K': self.amount['komplex']})
        dict.update({'common': self.result})
        dict.update(dict_month)
        dict.update(dict_year)

        return dict


data = Initial_Data()
