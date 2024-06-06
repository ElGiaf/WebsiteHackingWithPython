import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executeable_path="chromedriver.exe")
user = []
with open('user.txt','r') as file:
    user = file.read().splitlines()
    file.close()
driver = webdriver.Chrome(service=s)
website = 'https://github.com/login'
driver.get(website)
res = driver.find_element(By.ID, "login_field")
res.clear()
res.send_keys(user[0])

res = driver.find_element(By.ID, "password")
res.clear()
res.send_keys(user[1])

#time.sleep(10)
but = driver.find_element(By.NAME, "commit")
but.click()
websites = ["https://github.com/ElGiaf/WebsiteHackingWithPython"]
for website in websites:
    splitweb = website.split('/')
    print(splitweb)
    keys = ['key','secret','password']
    for key in keys:
        newweb = str('https://github.com/search?q=repo%3A'+splitweb[3]+'%2F'+splitweb[4]+'%20'+key+'&type=code')
        driver.get(newweb)
        element = driver.find_elements(By.CLASS_NAME,'Text-sc-17v1xeu-0')
        for i in element:
            res = i.text.lower()
            if key in res:
                print(res)


driver.quit()