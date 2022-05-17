from selenium import webdriver
# path = "/home/joao/chromedriver"
path = "./chromedriver"

driver = webdriver.Chrome(path)

driver.get('https://techwithtim.net')