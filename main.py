from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from decouple import Config, RepositoryEnv

DOTENV_FILE = '.env'
env_config = Config(RepositoryEnv(DOTENV_FILE))

PATH_CHROMEDRIVER = env_config('PATH_CHROMEDRIVER')
PAGE_HTML = env_config('PAGE_HTML')
EMAIL_LOGIN = env_config('EMAIL_LOGIN')
PASSWORD_LOGIN = env_config('PASSWORD_LOGIN')

driver = webdriver.Chrome(PATH_CHROMEDRIVER)

driver.get(PAGE_HTML)

if driver.title == "Login":
    element_email = driver.find_element_by_name("email")
    element_email.send_keys(EMAIL_LOGIN)

    element_senha = driver.find_element_by_name("password")
    element_senha.send_keys(PASSWORD_LOGIN)

    element_login = driver.find_element_by_id("submit")
    element_login.click()

driver.close() # tab
driver.quit()
