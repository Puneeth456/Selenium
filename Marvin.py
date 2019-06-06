from selenium import webdriver


Amma=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
Amma.get("http://172.40.10.107:8090")
Amma.find_element_by_name("username").send_keys("dhanya.rai@treebohotels.com")
Amma.find_element_by_name("password").send_keys("treebo135")
Amma.find_element_by_xpath("//button[@type='submit']").click()
