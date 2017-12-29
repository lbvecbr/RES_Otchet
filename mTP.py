# !/usr/bin/env python
# -*- coding: utf-8 -*-
# dimon

class TP(object):
    def __init__(self, nomerTP, nomer_schetchika, koeficient):
        self.__nomer_schetchika = nomer_schetchika
        self.__koeficient = koeficient
        self.__nomerTP = nomerTP


    @property
    def prediduschie(self):
        return self.__Prediduschie

    @prediduschie.setter
    def prediduschie(self, value):
        self.__Prediduschie = value    \

    @property
    def prediduschie(self):
        return self.__Prediduschie

    @prediduschie.setter
    def prediduschie(self, value):
        self.__Prediduschie = value



    @property
    def raznica(self):
        return self.__segodnjashnie - self.__prediduschie

    @property
    def real_raznica(self):
        return self.raznica * self.__koeficient




komplex =         TP("402", "0784180", 30)
cfg_grigorivske = TP("402", "0557402", 1)
mtf =             TP("219", "0780859", 30)
meh_tok =         TP("344", "0223889", 60)
stf =             TP("245", "0784148", 40)
meh_mastersk =    TP("209", "0466711", 1)
tr_br_1 =         TP("209", "0645465", 1)
tr_br_3 =         TP("246", "0065047", 1)
zernosklad =      TP("246", "0642837", 1)
stroiceh =        TP("244", "03157", 1)
kontora =         TP("218", "26459", 1)
lotok =           TP(" ", "43546557", 1)

