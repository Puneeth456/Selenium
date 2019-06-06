from selenium import webdriver

Chunk=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
Chunk.get("https://www.facebook.com/")
Chunk.find_element_by_id("u_0_j").send_keys("Puneeth")
Chunk.find_element_by_name("lastname").send_keys("B S")
Chunk.find_element_by_name("reg_email__").send_keys("9535468206")
Chunk.find_element_by_name("reg_passwd__").send_keys("preethiaunty")
Chunk.find_element_by_class_name("_58mt").click()
Chunk.find_element_by_name("websubmit").click()