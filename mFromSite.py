# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from docxtpl import DocxTemplate

login    = 'ivdmgen'
password = '1lbvecbr1'
url = 'https://ukrbilling.com/prom/ru'

browser = webdriver.Chrome()
browser.get(url)
login_input = browser.find_element_by_id('username')
pass_input = browser.find_element_by_id('password')
btn_enter = browser.find_element_by_name('commit')
login_input.send_keys(login)
pass_input.send_keys(password)
btn_enter.click()

link_to_readings = browser.find_element_by_xpath('.//*[@id="content"]/div/div[4]/div[1]/a')
link_to_readings.click()

L = browser.find_elements_by_xpath('//td[@class="left_half r_source_3"]')
list_of_prev_readings = [int(K.text[2:-1]) for K in L]
L = browser.find_elements_by_xpath('//td[@class="r_source_3 left_half"]')
list_of_now_readings = [int(K.text[2:-1]) for K in L]
L = browser.find_elements_by_xpath('//td[@class="number coef"]')
list_of_coeficients = [int(K.text) for K in L]
L = browser.find_elements_by_xpath('//td[@class="number calc_consumption"]')
list_of_calculates = [int(float(K.text)) for K in L]
list_of_middle_rezults = [int(x/y) for x, y in zip(list_of_calculates, list_of_coeficients)]


print(list_of_prev_readings)
print(list_of_now_readings)
print(list_of_coeficients)
print(list_of_calculates)
print(list_of_middle_rezults)

doc = DocxTemplate('res_template.docx')

dict = {}
dict_now = {'n'+str(i): K for i,K in enumerate(list_of_now_readings)}
dict_prew = {'p'+str(i): K for i,K in enumerate(list_of_prev_readings)}
dict.update(dict_now)
dict.update(dict_prew)
print(dict)
