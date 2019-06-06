from selenium import webdriver

India=webdriver.Chrome('C:/Users/Admin/Downloads/chromedriver.exe')
India.get("https://www.facebook.com/")
India.find_element_by_xpath("//input[@name='firstname']").send_keys("Puneeth")
India.find_element_by_xpath("//input[@name='lastname']").send_keys("B S")