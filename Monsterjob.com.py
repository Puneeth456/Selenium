from selenium import webdriver

mon=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
mon.get("https://www.monsterindia.com/")
mon.find_element_by_xpath("//span[text( )='Login']").click()
mon.find_element_by_id("signInName").send_keys("Puneeth")
mon.find_element_by_name("password").send_keys('chumma')
mon.find_element_by_xpath("//a[text( )='Forgot Password']").click()