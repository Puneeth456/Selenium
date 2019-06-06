from selenium import webdriver

qspider=webdriver.Chrome(executable_path='C:/Users/Admin/Downloads/chromedriver.exe')
qspider.get('https://www.naukri.com/')
qspider.find_element_by_id("login_Layer").click()
qspider.find_element_by_id("eLoginNew").send_keys("shivanpuneeth50@gmail.com")
qspider.find_element_by_id("pLogin").send_keys("Amma")
# qspider.find_element_by_xpath('//*[@id="lgnFrmNew"]/div[9]/button').click()
# qspider.find_element_by_class_name("blueBtn").click()
qspider.find_element_by_xpath("//button[@class='blueBtn']").click()

# https://www.quikr.com/QuikrX/Cart
