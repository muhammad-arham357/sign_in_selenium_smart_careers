from selenium import webdriver   
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

actions = ActionChains(driver)
driver.get("https://smartcareers.pk/register.aspx")

email_searchbox = driver.find_element(By.XPATH,'//*[@id="email"]')
email_searchbox.send_keys('XYZ@gmail.com')

pass_code = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[3]/div/input')
pass_code.send_keys('qwerty123')

conf_pass_code = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[4]/div/input')
conf_pass_code.send_keys('qwerty123')

user_name = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[5]/div/input')
user_name.send_keys('M.Arham')

father_name = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[6]/div/input')
father_name.send_keys('xyz')

cnic = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[7]/div/input')
cnic.send_keys('23689462081363486')

dropdown_gender = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[8]/div/select')
dropdown_select = Select(dropdown_gender)
dropdown_select.select_by_value("Male")

time.sleep(3)

date_of_birth_mon = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[9]/div[2]/select')
d_o_b_m_select = Select(date_of_birth_mon)
d_o_b_m_select.select_by_value("Aug")

time.sleep(3)

d_o_b_day = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[9]/div[1]/select')
d_o_b_day_select = Select(d_o_b_day)
d_o_b_day_select.select_by_value("28")

time.sleep(3)

b_year = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[9]/div[3]/select')
b_year_select = Select(b_year)
b_year_select.select_by_value("2009")

address = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[10]/div/input')
address.send_keys('3415 Oakwood Drive, Apt 3B, Springfield, IL 62711')

city = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[12]/div/select')
city_select = Select(city)
city_select.select_by_value("682")

postal_code = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[13]/div/input')
postal_code.send_keys('86319')

perm_addres = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[14]/div/input')
perm_addres.send_keys('3415 Oakwood Drive, Apt 3B, Springfield, IL 62711')

marker = driver.find_element(By.XPATH,"/html/body/form/div[3]/section/div/div/div[2]/div[15]/div/table/tbody/tr[2]/td/input")
marker.click()

domacile = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[16]/div/select')
domacile_select = Select(domacile)
domacile_select.select_by_value("Sind (U)")

cell_no = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[18]/div/input')
cell_no.send_keys('0394-109740912')

idk = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[19]/div/input')
idk.send_keys('90ba27f')

submit = driver.find_element(By.XPATH,'/html/body/form/div[3]/section/div/div/div[2]/div[20]/div[2]/div/input')
submit.click()



