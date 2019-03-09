from selenium import webdriver       #（1）

browser = webdriver.Firefox()        #（2）
browser.get('http://localhost:8000') #（3）

assert 'Django' in browser.title     #（4）
