from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'D:\PythonProject\webtest\bin\chromedriver.exe')  ## webdriver 경로 설정

driver.implicitly_wait(3)  ## 암시적 대기?

driver.get('https://www.naver.com')  ## 네이버 접속
print(driver.title)

sleep(5)

driver.quit()
