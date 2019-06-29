import time
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]").click()
time.sleep(5)
driver.find_element_by_xpath("//tr[7]/td[2]/input").send_keys("colima,mexicoa")
driver.find_element_by_xpath("//tr[9]/td[2]/input").send_keys("colima")
driver.find_element_by_xpath("//tr[5]/td/form/table/tbody/tr[10]/td[2]/input").send_keys("colima")
driver.find_element_by_xpath("//tr[11]/td[2]/input").send_keys("123456")
driver.find_element_by_xpath("//select/option[3]").click()   
time.sleep(3)
driver.find_element_by_xpath("//*[@id='email']").send_keys("andres.pacheco.io")
driver.find_element_by_xpath("//tr[15]/td[2]/input").send_keys("vetta.andres")
driver.find_element_by_xpath("//tr[16]/td[2]/input").send_keys("vetta.andres")
driver.find_element_by_name("register").click()
time.sleep(3)


driver.quit()