from selenium import webdriver

chumma=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
chumma.get("file:///C:/Users/Admin/Desktop/Demo%20Html.html")
chumma.find_element_by_id('123').send_keys('Puneeth')
chumma.find_element_by_id('456').send_keys('Amma')
chumma.find_element_by_name("log").click()