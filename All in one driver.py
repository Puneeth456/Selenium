from selenium import webdriver

browser='chrome'

if(browser=='chrome'):
    driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
elif(browser=='ff'):
    driver=webdriver.Firefox(executable_path="C:/Users/Admin/Downloads/geckodriver.exe")
elif(browser == 'ie'):
    driver=webdriver.Ie(executable_path="C:/Users/Admin/Downloads/IEDriverServer.exe")

