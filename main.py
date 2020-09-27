from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

''' Заходим в intra '''
login = 'login'
password = 'password'
path = r"/Users/dyoung/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.get ('https://signin.intra.42.fr/users/sign_in')
driver.find_element_by_id('user_login').send_keys(login)
driver.find_element_by_id('user_password').send_keys(password)
driver.find_element_by_id('user_password').send_keys(Keys.ENTER)

""" Выбираем Event"""
driver.find_element_by_class_name('event-button').click()

""" Регистрируемся на Event """
time.sleep(5)
driver.find_element_by_xpath('//*[@id="smartModal"]/div/div/div[3]/a').click()